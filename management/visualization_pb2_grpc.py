# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import visualization_pb2 as visualization__pb2


class VisualizationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTickets = channel.unary_unary(
                '/Visualization/GetTickets',
                request_serializer=visualization__pb2.TicketsRequest.SerializeToString,
                response_deserializer=visualization__pb2.TicketsResponse.FromString,
                )
        self.GetAirline = channel.unary_unary(
                '/Visualization/GetAirline',
                request_serializer=visualization__pb2.AirlineRequest.SerializeToString,
                response_deserializer=visualization__pb2.AirlineResponse.FromString,
                )
        self.AddTicket = channel.unary_unary(
                '/Visualization/AddTicket',
                request_serializer=visualization__pb2.Ticket.SerializeToString,
                response_deserializer=visualization__pb2.Ticket.FromString,
                )


class VisualizationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTickets(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAirline(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddTicket(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VisualizationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTickets': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTickets,
                    request_deserializer=visualization__pb2.TicketsRequest.FromString,
                    response_serializer=visualization__pb2.TicketsResponse.SerializeToString,
            ),
            'GetAirline': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAirline,
                    request_deserializer=visualization__pb2.AirlineRequest.FromString,
                    response_serializer=visualization__pb2.AirlineResponse.SerializeToString,
            ),
            'AddTicket': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTicket,
                    request_deserializer=visualization__pb2.Ticket.FromString,
                    response_serializer=visualization__pb2.Ticket.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Visualization', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Visualization(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTickets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Visualization/GetTickets',
            visualization__pb2.TicketsRequest.SerializeToString,
            visualization__pb2.TicketsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAirline(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Visualization/GetAirline',
            visualization__pb2.AirlineRequest.SerializeToString,
            visualization__pb2.AirlineResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddTicket(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Visualization/AddTicket',
            visualization__pb2.Ticket.SerializeToString,
            visualization__pb2.Ticket.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)