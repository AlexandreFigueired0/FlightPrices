from flask import Flask, jsonify
import grpc
import os
import time
import random
import psutil

from visualization_pb2 import Ticket, TicketsRequest, Airline, AirlineRequest
from visualization_pb2_grpc import VisualizationStub
from prometheus_client import start_http_server, Summary, Histogram, CONTENT_TYPE_LATEST, generate_latest, Counter, Gauge, CollectorRegistry

app = Flask(__name__)

# Connect to the database visualization service
database_visualization_host = os.getenv("DATABASE_VISUALIZATION_HOST", "localhost")
database_visualization_channel = grpc.insecure_channel(f"{database_visualization_host}:50051")
database_visualization_client = VisualizationStub(database_visualization_channel)

# prometheus metrics
request_counter = Counter("requests_counter_visualization", "Total number of requests of visualization")
cpu_usage = Gauge('cpu_usage_percent_visualization', 'CPU Usage Percentage of visualization')
memory_usage = Gauge('memory_usage_percent_visualization', 'Memory Usage Percentage of visualization')


@app.route("/api/visualization/tickets/<departure>/<arrival>", methods=["GET"])
def get_tickets_from_to(departure, arrival):
    request_counter.inc(1)
    tickets_request = TicketsRequest(
        departure_place=departure,
        arrival_place=arrival
    )

    tickets_response = database_visualization_client.GetTickets(tickets_request)

        # Helper function to convert a Ticket object into a dictionary
    def ticket_to_dict(ticket):
        return {
            "ticket_id": ticket.leg_id,
            "departure": ticket.departure_place,
            "arrival": ticket.arrival_place,
            "price": ticket.total_fare,
            "flight_date": ticket.flight_date,
            # Add other relevant fields here
        }

    # Convert each Ticket object in the response to a dictionary
    tickets_list = [ticket_to_dict(ticket) for ticket in tickets_response.tickets]

    return jsonify({ "tickets": tickets_list })

@app.route("/api/visualization/airlines/<airline_code>", methods=["GET"])
def get_airline_details(airline_code):
    request_counter.inc(1)
    airline_request = AirlineRequest(airline_code=airline_code)
    
    airline_response = database_visualization_client.GetAirline(airline_request)

    return jsonify({"airlineCode": str(airline_response.airline.airline_code), "airlineName": str(airline_response.airline.airline_name)})

@app.route("/api/visualization/liveness-check", methods=['GET'])
def liveness_check():
    return "ok",200

# @app.route("/api/visualization/metrics", methods=['GET'])
# def metrics():
#     return "ok",200    

@app.route("/metrics", methods=['GET'])
def prometheus_metrics():
    cpu_usage.set(psutil.cpu_percent())
    memory_usage.set(psutil.virtual_memory().percent)
    return generate_latest() 