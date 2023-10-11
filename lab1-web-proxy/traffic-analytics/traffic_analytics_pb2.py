# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: traffic_analytics.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17traffic_analytics.proto\x12\tanalytics\"\x90\x01\n\x17TrafficDataForAnalytics\x12\x17\n\x0fintersection_id\x18\x01 \x01(\x05\x12\x17\n\x0fsignal_status_1\x18\x02 \x01(\x05\x12\x15\n\rvehicle_count\x18\x03 \x01(\x05\x12\x10\n\x08incident\x18\x04 \x01(\x08\x12\x0c\n\x04\x64\x61te\x18\x05 \x01(\t\x12\x0c\n\x04time\x18\x06 \x01(\t\"9\n&TrafficDataForAnalyticsReceiveResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\":\n\x1fIntersectionRequestForAnalytics\x12\x17\n\x0fintersection_id\x18\x01 \x01(\x05\"\x94\x01\n\x18TrafficAnalyticsResponse\x12\x17\n\x0fintersection_id\x18\x01 \x01(\x05\x12\x11\n\ttimestamp\x18\x02 \x01(\t\x12\x1d\n\x15\x61verage_vehicle_count\x18\x03 \x01(\x01\x12\x12\n\npeak_hours\x18\x04 \x01(\t\x12\x19\n\x11\x61verage_incidents\x18\x05 \x01(\x02\x32\xc0\x03\n\x10TrafficAnalytics\x12p\n\x17ReceiveDataForAnalytics\x12\".analytics.TrafficDataForAnalytics\x1a\x31.analytics.TrafficDataForAnalyticsReceiveResponse\x12\x65\n\x12GetTodayStatistics\x12*.analytics.IntersectionRequestForAnalytics\x1a#.analytics.TrafficAnalyticsResponse\x12h\n\x15GetLastWeekStatistics\x12*.analytics.IntersectionRequestForAnalytics\x1a#.analytics.TrafficAnalyticsResponse\x12i\n\x16GetNextWeekPredictions\x12*.analytics.IntersectionRequestForAnalytics\x1a#.analytics.TrafficAnalyticsResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'traffic_analytics_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TRAFFICDATAFORANALYTICS']._serialized_start=39
  _globals['_TRAFFICDATAFORANALYTICS']._serialized_end=183
  _globals['_TRAFFICDATAFORANALYTICSRECEIVERESPONSE']._serialized_start=185
  _globals['_TRAFFICDATAFORANALYTICSRECEIVERESPONSE']._serialized_end=242
  _globals['_INTERSECTIONREQUESTFORANALYTICS']._serialized_start=244
  _globals['_INTERSECTIONREQUESTFORANALYTICS']._serialized_end=302
  _globals['_TRAFFICANALYTICSRESPONSE']._serialized_start=305
  _globals['_TRAFFICANALYTICSRESPONSE']._serialized_end=453
  _globals['_TRAFFICANALYTICS']._serialized_start=456
  _globals['_TRAFFICANALYTICS']._serialized_end=904
# @@protoc_insertion_point(module_scope)