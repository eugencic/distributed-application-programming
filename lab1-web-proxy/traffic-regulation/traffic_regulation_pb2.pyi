from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TrafficDataForLogs(_message.Message):
    __slots__ = ["intersection_id", "signal_status_1", "vehicle_count", "incident", "date", "time"]
    INTERSECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_STATUS_1_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    INCIDENT_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    intersection_id: int
    signal_status_1: int
    vehicle_count: int
    incident: bool
    date: str
    time: str
    def __init__(self, intersection_id: _Optional[int] = ..., signal_status_1: _Optional[int] = ..., vehicle_count: _Optional[int] = ..., incident: bool = ..., date: _Optional[str] = ..., time: _Optional[str] = ...) -> None: ...

class TrafficDataForLogsReceiveResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class IntersectionRequestForLogs(_message.Message):
    __slots__ = ["intersection_id"]
    INTERSECTION_ID_FIELD_NUMBER: _ClassVar[int]
    intersection_id: int
    def __init__(self, intersection_id: _Optional[int] = ...) -> None: ...

class TrafficRegulationResponse(_message.Message):
    __slots__ = ["intersection_id", "timestamp"]
    INTERSECTION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    intersection_id: int
    timestamp: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, intersection_id: _Optional[int] = ..., timestamp: _Optional[_Iterable[str]] = ...) -> None: ...