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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13visualization.proto\"q\n\x06Ticket\x12\x0e\n\x06leg_id\x18\x01 \x01(\t\x12\x17\n\x0f\x64\x65parture_place\x18\x02 \x01(\t\x12\x15\n\rarrival_place\x18\x03 \x01(\t\x12\x13\n\x0b\x66light_date\x18\x04 \x01(\t\x12\x12\n\ntotal_fare\x18\x05 \x01(\x02\"5\n\x07\x41irline\x12\x14\n\x0c\x61irline_code\x18\x01 \x01(\t\x12\x14\n\x0c\x61irline_name\x18\x02 \x01(\t\"@\n\x0eTicketsRequest\x12\x17\n\x0f\x64\x65parture_place\x18\x01 \x01(\t\x12\x15\n\rarrival_place\x18\x02 \x01(\t\"+\n\x0fTicketsResponse\x12\x18\n\x07tickets\x18\x01 \x03(\x0b\x32\x07.Ticket\"&\n\x0e\x41irlineRequest\x12\x14\n\x0c\x61irline_code\x18\x01 \x01(\t\",\n\x0f\x41irlineResponse\x12\x19\n\x07\x61irline\x18\x01 \x01(\x0b\x32\x08.Airline2q\n\rVisualization\x12/\n\nGetTickets\x12\x0f.TicketsRequest\x1a\x10.TicketsResponse\x12/\n\nGetAirline\x12\x0f.AirlineRequest\x1a\x10.AirlineResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'visualization_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TICKET']._serialized_start=23
  _globals['_TICKET']._serialized_end=136
  _globals['_AIRLINE']._serialized_start=138
  _globals['_AIRLINE']._serialized_end=191
  _globals['_TICKETSREQUEST']._serialized_start=193
  _globals['_TICKETSREQUEST']._serialized_end=257
  _globals['_TICKETSRESPONSE']._serialized_start=259
  _globals['_TICKETSRESPONSE']._serialized_end=302
  _globals['_AIRLINEREQUEST']._serialized_start=304
  _globals['_AIRLINEREQUEST']._serialized_end=342
  _globals['_AIRLINERESPONSE']._serialized_start=344
  _globals['_AIRLINERESPONSE']._serialized_end=388
  _globals['_VISUALIZATION']._serialized_start=390
  _globals['_VISUALIZATION']._serialized_end=503
# @@protoc_insertion_point(module_scope)
