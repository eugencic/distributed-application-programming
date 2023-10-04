from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TrafficData(_message.Message):
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

class TrafficDataReceiveResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class IntersectionRequest(_message.Message):
    __slots__ = ["intersection_id"]
    INTERSECTION_ID_FIELD_NUMBER: _ClassVar[int]
    intersection_id: int
    def __init__(self, intersection_id: _Optional[int] = ...) -> None: ...

class TrafficAnalytics(_message.Message):
    __slots__ = ["intersection_id", "timestamp", "average_vehicle_count", "traffic_density", "peak_hours", "incidents"]
    INTERSECTION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_VEHICLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_DENSITY_FIELD_NUMBER: _ClassVar[int]
    PEAK_HOURS_FIELD_NUMBER: _ClassVar[int]
    INCIDENTS_FIELD_NUMBER: _ClassVar[int]
    intersection_id: int
    timestamp: str
    average_vehicle_count: float
    traffic_density: str
    peak_hours: _containers.RepeatedScalarFieldContainer[str]
    incidents: int
    def __init__(self, intersection_id: _Optional[int] = ..., timestamp: _Optional[str] = ..., average_vehicle_count: _Optional[float] = ..., traffic_density: _Optional[str] = ..., peak_hours: _Optional[_Iterable[str]] = ..., incidents: _Optional[int] = ...) -> None: ...
