# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: traffic_regulation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18traffic_regulation.proto\x12\x04main\"\x8b\x01\n\x12TrafficDataForLogs\x12\x17\n\x0fintersection_id\x18\x01 \x01(\x05\x12\x17\n\x0fsignal_status_1\x18\x02 \x01(\x05\x12\x15\n\rvehicle_count\x18\x03 \x01(\x05\x12\x10\n\x08incident\x18\x04 \x01(\x08\x12\x0c\n\x04\x64\x61te\x18\x05 \x01(\t\x12\x0c\n\x04time\x18\x06 \x01(\t\"4\n!TrafficDataForLogsReceiveResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"5\n\x1aIntersectionRequestForLogs\x12\x17\n\x0fintersection_id\x18\x01 \x01(\x05\"B\n\x19TrafficRegulationResponse\x12\x17\n\x0fintersection_id\x18\x01 \x01(\x05\x12\x0c\n\x04logs\x18\x02 \x03(\t2\xa3\x02\n\x11TrafficRegulation\x12W\n\x12ReceiveDataForLogs\x12\x18.main.TrafficDataForLogs\x1a\'.main.TrafficDataForLogsReceiveResponse\x12X\n\x13GetTodayControlLogs\x12 .main.IntersectionRequestForLogs\x1a\x1f.main.TrafficRegulationResponse\x12[\n\x16GetLastWeekControlLogs\x12 .main.IntersectionRequestForLogs\x1a\x1f.main.TrafficRegulationResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'traffic_regulation_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TRAFFICDATAFORLOGS']._serialized_start=35
  _globals['_TRAFFICDATAFORLOGS']._serialized_end=174
  _globals['_TRAFFICDATAFORLOGSRECEIVERESPONSE']._serialized_start=176
  _globals['_TRAFFICDATAFORLOGSRECEIVERESPONSE']._serialized_end=228
  _globals['_INTERSECTIONREQUESTFORLOGS']._serialized_start=230
  _globals['_INTERSECTIONREQUESTFORLOGS']._serialized_end=283
  _globals['_TRAFFICREGULATIONRESPONSE']._serialized_start=285
  _globals['_TRAFFICREGULATIONRESPONSE']._serialized_end=351
  _globals['_TRAFFICREGULATION']._serialized_start=354
  _globals['_TRAFFICREGULATION']._serialized_end=645
# @@protoc_insertion_point(module_scope)
