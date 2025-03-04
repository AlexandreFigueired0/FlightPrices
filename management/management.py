from flask import Flask, request
import grpc
import os
import psutil

from visualization_pb2 import Ticket, Airline, VisualizationInsertionRequest, VisualizationDeleteRequest
from visualization_pb2_grpc import VisualizationStub
from ranking_pb2 import RankingInsertionRequest, RankingDeleteRequest, AirlineRanking
from ranking_pb2_grpc import RankingStub
from prometheus_client import generate_latest, Counter, Gauge

# app = Flask(__name__)

# Connect to the database visualization service
database_visualization_host = os.getenv("DATABASE_VISUALIZATION_HOST", "localhost")
database_visualization_channel = grpc.insecure_channel(f"{database_visualization_host}:50051")
database_visualization_client = VisualizationStub(database_visualization_channel)

# Connect to the database ranking service
database_ranking_host = os.getenv("DATABASE_RANKING_HOST", "localhost")
database_ranking_channel = grpc.insecure_channel(f"{database_ranking_host}:50052")
database_ranking_client = RankingStub(database_ranking_channel)

app = Flask(__name__)


# metrics
request_counter = Counter("requests_counter_management", "Total number of requests of management")
cpu_usage = Gauge('cpu_usage_percent_management', 'CPU Usage Percentage of management')
memory_usage = Gauge('memory_usage_percent_management', 'Memory Usage Percentage of management')


@app.route("/api/management/tickets", methods=['POST'])
def add_tickets():
    request_counter.inc(1)
    request_body = request.json

    ticket_body = request_body["ticket"]
    airlines_body = request_body["airlines"]

    ticket = Ticket(
        leg_id=ticket_body['leg_id'],
        departure_place=ticket_body['departure_place'],
        arrival_place=ticket_body['arrival_place'],
        flight_date=ticket_body['flight_date'],
        total_fare=ticket_body['total_fare'],
        travel_duration=ticket_body['travel_duration'],
        total_travel_distance=ticket_body['total_travel_distance'],
        is_refundable=ticket_body['is_refundable'],
        is_non_stop=ticket_body['is_non_stop']
    )

    airlines = []
    airlinesRanking = []
    for airline_body in airlines_body:
        airline = Airline(
            airline_code=airline_body["airline_code"],
            airline_name=airline_body["airline_name"]
        )
        airlineRanking = AirlineRanking(
            airline_code=airline_body["airline_code"],
            airline_name=airline_body["airline_name"]
        )

        airlines.append(airline)
        airlinesRanking.append(airlineRanking)

    visualization_insertion_request = VisualizationInsertionRequest(ticket=ticket, airlines=airlines)
    ranking_insertion_request = RankingInsertionRequest(
                                    leg_id=ticket.leg_id,
                                    price=ticket.total_fare,
                                    airlines=airlinesRanking
                                    )

    # Add the ticket to the tickets database
    tickets_response = database_visualization_client.AddTicket(visualization_insertion_request)
    # Add to the ranking database
    ranking_response = database_ranking_client.AddAirlinePrice(ranking_insertion_request)

    if tickets_response == "error":
        return "Error adding ticket to the visualization database"
    if ranking_response == "error":
        return "Error adding airline price to the ranking database"

    return "Ticket added successfully"


@app.route("/api/management/tickets/<leg_id>", methods=['DELETE'])
def delete_ticket(leg_id):
    request_counter.inc(1)

    # Delete the ticket from the tickets database
    # tickets_response = database_visualization_client.DeleteTicket(TicketsRequest(ticket_id=ticketId))

    # Remove ticket from ranking database
    ranking_delete_request = RankingDeleteRequest(leg_id=leg_id)
    ranking_delete_response = database_ranking_client.DeleteTicket(ranking_delete_request)

    if ranking_delete_response == "error":
        return "Error deleting ticket from the ranking database"

    visualization_delete_request = VisualizationDeleteRequest(leg_id=leg_id)
    visualization_delete_response = database_visualization_client.DeleteTicket(visualization_delete_request)

    if visualization_delete_response == "error":
        return "Error deleting ticket from the visualization database"

    return "Ticket deleted successfully"


@app.route("/api/management/liveness-check", methods=['GET'])
def liveness_check():
    return "ok", 200


@app.route("/metrics", methods=['GET'])
def prometheus_metrics():
    cpu_usage.set(psutil.cpu_percent())
    memory_usage.set(psutil.virtual_memory().percent)
    return generate_latest()
