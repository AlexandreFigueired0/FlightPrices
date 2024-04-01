# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: visualization.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13visualization.proto\"\xd5\x01\n\x06Ticket\x12\x0e\n\x06leg_id\x18\x01 \x01(\t\x12\x17\n\x0f\x64\x65parture_place\x18\x02 \x01(\t\x12\x15\n\rarrival_place\x18\x03 \x01(\t\x12\x13\n\x0b\x66light_date\x18\x04 \x01(\t\x12\x12\n\ntotal_fare\x18\x05 \x01(\x02\x12\x17\n\x0ftravel_duration\x18\x06 \x01(\t\x12\x1d\n\x15total_travel_distance\x18\x07 \x01(\x02\x12\x15\n\ris_refundable\x18\x08 \x01(\x08\x12\x13\n\x0bis_non_stop\x18\t \x01(\x08\"5\n\x07\x41irline\x12\x14\n\x0c\x61irline_code\x18\x01 \x01(\t\x12\x14\n\x0c\x61irline_name\x18\x02 \x01(\t\"T\n\x1dVisualizationInsertionRequest\x12\x17\n\x06ticket\x18\x01 \x01(\x0b\x32\x07.Ticket\x12\x1a\n\x08\x61irlines\x18\x02 \x03(\x0b\x32\x08.Airline\"6\n\x1eVisualizationInsertionResponse\x12\x14\n\x0cquery_status\x18\x01 \x01(\t\",\n\x1aVisualizationDeleteRequest\x12\x0e\n\x06leg_id\x18\x01 \x01(\t\"3\n\x1bVisualizationDeleteResponse\x12\x14\n\x0cquery_status\x18\x01 \x01(\t\"@\n\x0eTicketsRequest\x12\x17\n\x0f\x64\x65parture_place\x18\x01 \x01(\t\x12\x15\n\rarrival_place\x18\x02 \x01(\t\"+\n\x0fTicketsResponse\x12\x18\n\x07tickets\x18\x01 \x03(\x0b\x32\x07.Ticket\"&\n\x0e\x41irlineRequest\x12\x14\n\x0c\x61irline_code\x18\x01 \x01(\t\",\n\x0f\x41irlineResponse\x12\x19\n\x07\x61irline\x18\x01 \x01(\x0b\x32\x08.Airline2\x8a\x02\n\rVisualization\x12/\n\nGetTickets\x12\x0f.TicketsRequest\x1a\x10.TicketsResponse\x12/\n\nGetAirline\x12\x0f.AirlineRequest\x1a\x10.AirlineResponse\x12L\n\tAddTicket\x12\x1e.VisualizationInsertionRequest\x1a\x1f.VisualizationInsertionResponse\x12I\n\x0c\x44\x65leteTicket\x12\x1b.VisualizationDeleteRequest\x1a\x1c.VisualizationDeleteResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'visualization_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TICKET']._serialized_start=24
  _globals['_TICKET']._serialized_end=237
  _globals['_AIRLINE']._serialized_start=239
  _globals['_AIRLINE']._serialized_end=292
  _globals['_VISUALIZATIONINSERTIONREQUEST']._serialized_start=294
  _globals['_VISUALIZATIONINSERTIONREQUEST']._serialized_end=378
  _globals['_VISUALIZATIONINSERTIONRESPONSE']._serialized_start=380
  _globals['_VISUALIZATIONINSERTIONRESPONSE']._serialized_end=434
  _globals['_VISUALIZATIONDELETEREQUEST']._serialized_start=436
  _globals['_VISUALIZATIONDELETEREQUEST']._serialized_end=480
  _globals['_VISUALIZATIONDELETERESPONSE']._serialized_start=482
  _globals['_VISUALIZATIONDELETERESPONSE']._serialized_end=533
  _globals['_TICKETSREQUEST']._serialized_start=535
  _globals['_TICKETSREQUEST']._serialized_end=599
  _globals['_TICKETSRESPONSE']._serialized_start=601
  _globals['_TICKETSRESPONSE']._serialized_end=644
  _globals['_AIRLINEREQUEST']._serialized_start=646
  _globals['_AIRLINEREQUEST']._serialized_end=684
  _globals['_AIRLINERESPONSE']._serialized_start=686
  _globals['_AIRLINERESPONSE']._serialized_end=730
  _globals['_VISUALIZATION']._serialized_start=733
  _globals['_VISUALIZATION']._serialized_end=999
# @@protoc_insertion_point(module_scope)
