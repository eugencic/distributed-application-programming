// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.31.0
// 	protoc        v4.24.4
// source: traffic_regulation.proto

package __

import (
	_ "google.golang.org/genproto/googleapis/api/annotations"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type TrafficDataForLogs struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	IntersectionId int32  `protobuf:"varint,1,opt,name=intersection_id,json=intersectionId,proto3" json:"intersection_id,omitempty"`
	SignalStatus_1 int32  `protobuf:"varint,2,opt,name=signal_status_1,json=signalStatus1,proto3" json:"signal_status_1,omitempty"`
	VehicleCount   int32  `protobuf:"varint,3,opt,name=vehicle_count,json=vehicleCount,proto3" json:"vehicle_count,omitempty"`
	Incident       bool   `protobuf:"varint,4,opt,name=incident,proto3" json:"incident,omitempty"`
	Date           string `protobuf:"bytes,5,opt,name=date,proto3" json:"date,omitempty"`
	Time           string `protobuf:"bytes,6,opt,name=time,proto3" json:"time,omitempty"`
}

func (x *TrafficDataForLogs) Reset() {
	*x = TrafficDataForLogs{}
	if protoimpl.UnsafeEnabled {
		mi := &file_traffic_regulation_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *TrafficDataForLogs) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TrafficDataForLogs) ProtoMessage() {}

func (x *TrafficDataForLogs) ProtoReflect() protoreflect.Message {
	mi := &file_traffic_regulation_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TrafficDataForLogs.ProtoReflect.Descriptor instead.
func (*TrafficDataForLogs) Descriptor() ([]byte, []int) {
	return file_traffic_regulation_proto_rawDescGZIP(), []int{0}
}

func (x *TrafficDataForLogs) GetIntersectionId() int32 {
	if x != nil {
		return x.IntersectionId
	}
	return 0
}

func (x *TrafficDataForLogs) GetSignalStatus_1() int32 {
	if x != nil {
		return x.SignalStatus_1
	}
	return 0
}

func (x *TrafficDataForLogs) GetVehicleCount() int32 {
	if x != nil {
		return x.VehicleCount
	}
	return 0
}

func (x *TrafficDataForLogs) GetIncident() bool {
	if x != nil {
		return x.Incident
	}
	return false
}

func (x *TrafficDataForLogs) GetDate() string {
	if x != nil {
		return x.Date
	}
	return ""
}

func (x *TrafficDataForLogs) GetTime() string {
	if x != nil {
		return x.Time
	}
	return ""
}

type TrafficDataForLogsReceiveResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Message string `protobuf:"bytes,1,opt,name=message,proto3" json:"message,omitempty"`
}

func (x *TrafficDataForLogsReceiveResponse) Reset() {
	*x = TrafficDataForLogsReceiveResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_traffic_regulation_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *TrafficDataForLogsReceiveResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TrafficDataForLogsReceiveResponse) ProtoMessage() {}

func (x *TrafficDataForLogsReceiveResponse) ProtoReflect() protoreflect.Message {
	mi := &file_traffic_regulation_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TrafficDataForLogsReceiveResponse.ProtoReflect.Descriptor instead.
func (*TrafficDataForLogsReceiveResponse) Descriptor() ([]byte, []int) {
	return file_traffic_regulation_proto_rawDescGZIP(), []int{1}
}

func (x *TrafficDataForLogsReceiveResponse) GetMessage() string {
	if x != nil {
		return x.Message
	}
	return ""
}

type IntersectionRequestForLogs struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	IntersectionId int32 `protobuf:"varint,1,opt,name=intersection_id,json=intersectionId,proto3" json:"intersection_id,omitempty"`
}

func (x *IntersectionRequestForLogs) Reset() {
	*x = IntersectionRequestForLogs{}
	if protoimpl.UnsafeEnabled {
		mi := &file_traffic_regulation_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *IntersectionRequestForLogs) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*IntersectionRequestForLogs) ProtoMessage() {}

func (x *IntersectionRequestForLogs) ProtoReflect() protoreflect.Message {
	mi := &file_traffic_regulation_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use IntersectionRequestForLogs.ProtoReflect.Descriptor instead.
func (*IntersectionRequestForLogs) Descriptor() ([]byte, []int) {
	return file_traffic_regulation_proto_rawDescGZIP(), []int{2}
}

func (x *IntersectionRequestForLogs) GetIntersectionId() int32 {
	if x != nil {
		return x.IntersectionId
	}
	return 0
}

type TrafficRegulationResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	IntersectionId int32    `protobuf:"varint,1,opt,name=intersection_id,json=intersectionId,proto3" json:"intersection_id,omitempty"`
	Timestamp      []string `protobuf:"bytes,2,rep,name=timestamp,proto3" json:"timestamp,omitempty"`
}

func (x *TrafficRegulationResponse) Reset() {
	*x = TrafficRegulationResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_traffic_regulation_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *TrafficRegulationResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*TrafficRegulationResponse) ProtoMessage() {}

func (x *TrafficRegulationResponse) ProtoReflect() protoreflect.Message {
	mi := &file_traffic_regulation_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use TrafficRegulationResponse.ProtoReflect.Descriptor instead.
func (*TrafficRegulationResponse) Descriptor() ([]byte, []int) {
	return file_traffic_regulation_proto_rawDescGZIP(), []int{3}
}

func (x *TrafficRegulationResponse) GetIntersectionId() int32 {
	if x != nil {
		return x.IntersectionId
	}
	return 0
}

func (x *TrafficRegulationResponse) GetTimestamp() []string {
	if x != nil {
		return x.Timestamp
	}
	return nil
}

var File_traffic_regulation_proto protoreflect.FileDescriptor

var file_traffic_regulation_proto_rawDesc = []byte{
	0x0a, 0x18, 0x74, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x5f, 0x72, 0x65, 0x67, 0x75, 0x6c, 0x61,
	0x74, 0x69, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x0a, 0x72, 0x65, 0x67, 0x75,
	0x6c, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x1a, 0x1c, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x61,
	0x70, 0x69, 0x2f, 0x61, 0x6e, 0x6e, 0x6f, 0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x22, 0xce, 0x01, 0x0a, 0x12, 0x54, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63,
	0x44, 0x61, 0x74, 0x61, 0x46, 0x6f, 0x72, 0x4c, 0x6f, 0x67, 0x73, 0x12, 0x27, 0x0a, 0x0f, 0x69,
	0x6e, 0x74, 0x65, 0x72, 0x73, 0x65, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x01,
	0x20, 0x01, 0x28, 0x05, 0x52, 0x0e, 0x69, 0x6e, 0x74, 0x65, 0x72, 0x73, 0x65, 0x63, 0x74, 0x69,
	0x6f, 0x6e, 0x49, 0x64, 0x12, 0x26, 0x0a, 0x0f, 0x73, 0x69, 0x67, 0x6e, 0x61, 0x6c, 0x5f, 0x73,
	0x74, 0x61, 0x74, 0x75, 0x73, 0x5f, 0x31, 0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x52, 0x0d, 0x73,
	0x69, 0x67, 0x6e, 0x61, 0x6c, 0x53, 0x74, 0x61, 0x74, 0x75, 0x73, 0x31, 0x12, 0x23, 0x0a, 0x0d,
	0x76, 0x65, 0x68, 0x69, 0x63, 0x6c, 0x65, 0x5f, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x18, 0x03, 0x20,
	0x01, 0x28, 0x05, 0x52, 0x0c, 0x76, 0x65, 0x68, 0x69, 0x63, 0x6c, 0x65, 0x43, 0x6f, 0x75, 0x6e,
	0x74, 0x12, 0x1a, 0x0a, 0x08, 0x69, 0x6e, 0x63, 0x69, 0x64, 0x65, 0x6e, 0x74, 0x18, 0x04, 0x20,
	0x01, 0x28, 0x08, 0x52, 0x08, 0x69, 0x6e, 0x63, 0x69, 0x64, 0x65, 0x6e, 0x74, 0x12, 0x12, 0x0a,
	0x04, 0x64, 0x61, 0x74, 0x65, 0x18, 0x05, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x64, 0x61, 0x74,
	0x65, 0x12, 0x12, 0x0a, 0x04, 0x74, 0x69, 0x6d, 0x65, 0x18, 0x06, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x04, 0x74, 0x69, 0x6d, 0x65, 0x22, 0x3d, 0x0a, 0x21, 0x54, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63,
	0x44, 0x61, 0x74, 0x61, 0x46, 0x6f, 0x72, 0x4c, 0x6f, 0x67, 0x73, 0x52, 0x65, 0x63, 0x65, 0x69,
	0x76, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x18, 0x0a, 0x07, 0x6d, 0x65,
	0x73, 0x73, 0x61, 0x67, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x07, 0x6d, 0x65, 0x73,
	0x73, 0x61, 0x67, 0x65, 0x22, 0x45, 0x0a, 0x1a, 0x49, 0x6e, 0x74, 0x65, 0x72, 0x73, 0x65, 0x63,
	0x74, 0x69, 0x6f, 0x6e, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x46, 0x6f, 0x72, 0x4c, 0x6f,
	0x67, 0x73, 0x12, 0x27, 0x0a, 0x0f, 0x69, 0x6e, 0x74, 0x65, 0x72, 0x73, 0x65, 0x63, 0x74, 0x69,
	0x6f, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x05, 0x52, 0x0e, 0x69, 0x6e, 0x74,
	0x65, 0x72, 0x73, 0x65, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x49, 0x64, 0x22, 0x62, 0x0a, 0x19, 0x54,
	0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x52, 0x65, 0x67, 0x75, 0x6c, 0x61, 0x74, 0x69, 0x6f, 0x6e,
	0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x27, 0x0a, 0x0f, 0x69, 0x6e, 0x74, 0x65,
	0x72, 0x73, 0x65, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x05, 0x52, 0x0e, 0x69, 0x6e, 0x74, 0x65, 0x72, 0x73, 0x65, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x49,
	0x64, 0x12, 0x1c, 0x0a, 0x09, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x18, 0x02,
	0x20, 0x03, 0x28, 0x09, 0x52, 0x09, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x32,
	0xc9, 0x03, 0x0a, 0x11, 0x54, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x52, 0x65, 0x67, 0x75, 0x6c,
	0x61, 0x74, 0x69, 0x6f, 0x6e, 0x12, 0x90, 0x01, 0x0a, 0x12, 0x52, 0x65, 0x63, 0x65, 0x69, 0x76,
	0x65, 0x44, 0x61, 0x74, 0x61, 0x46, 0x6f, 0x72, 0x4c, 0x6f, 0x67, 0x73, 0x12, 0x1e, 0x2e, 0x72,
	0x65, 0x67, 0x75, 0x6c, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x2e, 0x54, 0x72, 0x61, 0x66, 0x66, 0x69,
	0x63, 0x44, 0x61, 0x74, 0x61, 0x46, 0x6f, 0x72, 0x4c, 0x6f, 0x67, 0x73, 0x1a, 0x2d, 0x2e, 0x72,
	0x65, 0x67, 0x75, 0x6c, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x2e, 0x54, 0x72, 0x61, 0x66, 0x66, 0x69,
	0x63, 0x44, 0x61, 0x74, 0x61, 0x46, 0x6f, 0x72, 0x4c, 0x6f, 0x67, 0x73, 0x52, 0x65, 0x63, 0x65,
	0x69, 0x76, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x2b, 0x82, 0xd3, 0xe4,
	0x93, 0x02, 0x25, 0x3a, 0x01, 0x2a, 0x22, 0x20, 0x2f, 0x72, 0x65, 0x63, 0x65, 0x69, 0x76, 0x65,
	0x5f, 0x64, 0x61, 0x74, 0x61, 0x5f, 0x66, 0x6f, 0x72, 0x5f, 0x61, 0x6e, 0x61, 0x6c, 0x79, 0x74,
	0x69, 0x63, 0x73, 0x5f, 0x6c, 0x6f, 0x67, 0x73, 0x12, 0x8b, 0x01, 0x0a, 0x13, 0x47, 0x65, 0x74,
	0x54, 0x6f, 0x64, 0x61, 0x79, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x6f, 0x6c, 0x4c, 0x6f, 0x67, 0x73,
	0x12, 0x26, 0x2e, 0x72, 0x65, 0x67, 0x75, 0x6c, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x2e, 0x49, 0x6e,
	0x74, 0x65, 0x72, 0x73, 0x65, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73,
	0x74, 0x46, 0x6f, 0x72, 0x4c, 0x6f, 0x67, 0x73, 0x1a, 0x25, 0x2e, 0x72, 0x65, 0x67, 0x75, 0x6c,
	0x61, 0x74, 0x69, 0x6f, 0x6e, 0x2e, 0x54, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x52, 0x65, 0x67,
	0x75, 0x6c, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22,
	0x25, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x1f, 0x3a, 0x01, 0x2a, 0x22, 0x1a, 0x2f, 0x67, 0x65, 0x74,
	0x5f, 0x74, 0x6f, 0x64, 0x61, 0x79, 0x5f, 0x73, 0x74, 0x61, 0x74, 0x69, 0x73, 0x74, 0x69, 0x63,
	0x73, 0x5f, 0x6c, 0x6f, 0x67, 0x73, 0x12, 0x92, 0x01, 0x0a, 0x16, 0x47, 0x65, 0x74, 0x4c, 0x61,
	0x73, 0x74, 0x57, 0x65, 0x65, 0x6b, 0x43, 0x6f, 0x6e, 0x74, 0x72, 0x6f, 0x6c, 0x4c, 0x6f, 0x67,
	0x73, 0x12, 0x26, 0x2e, 0x72, 0x65, 0x67, 0x75, 0x6c, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x2e, 0x49,
	0x6e, 0x74, 0x65, 0x72, 0x73, 0x65, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x65, 0x71, 0x75, 0x65,
	0x73, 0x74, 0x46, 0x6f, 0x72, 0x4c, 0x6f, 0x67, 0x73, 0x1a, 0x25, 0x2e, 0x72, 0x65, 0x67, 0x75,
	0x6c, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x2e, 0x54, 0x72, 0x61, 0x66, 0x66, 0x69, 0x63, 0x52, 0x65,
	0x67, 0x75, 0x6c, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65,
	0x22, 0x29, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x23, 0x3a, 0x01, 0x2a, 0x22, 0x1e, 0x2f, 0x67, 0x65,
	0x74, 0x5f, 0x6c, 0x61, 0x73, 0x74, 0x5f, 0x77, 0x65, 0x65, 0x6b, 0x5f, 0x73, 0x74, 0x61, 0x74,
	0x69, 0x73, 0x74, 0x69, 0x63, 0x73, 0x5f, 0x6c, 0x6f, 0x67, 0x73, 0x42, 0x03, 0x5a, 0x01, 0x2e,
	0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_traffic_regulation_proto_rawDescOnce sync.Once
	file_traffic_regulation_proto_rawDescData = file_traffic_regulation_proto_rawDesc
)

func file_traffic_regulation_proto_rawDescGZIP() []byte {
	file_traffic_regulation_proto_rawDescOnce.Do(func() {
		file_traffic_regulation_proto_rawDescData = protoimpl.X.CompressGZIP(file_traffic_regulation_proto_rawDescData)
	})
	return file_traffic_regulation_proto_rawDescData
}

var file_traffic_regulation_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_traffic_regulation_proto_goTypes = []interface{}{
	(*TrafficDataForLogs)(nil),                // 0: regulation.TrafficDataForLogs
	(*TrafficDataForLogsReceiveResponse)(nil), // 1: regulation.TrafficDataForLogsReceiveResponse
	(*IntersectionRequestForLogs)(nil),        // 2: regulation.IntersectionRequestForLogs
	(*TrafficRegulationResponse)(nil),         // 3: regulation.TrafficRegulationResponse
}
var file_traffic_regulation_proto_depIdxs = []int32{
	0, // 0: regulation.TrafficRegulation.ReceiveDataForLogs:input_type -> regulation.TrafficDataForLogs
	2, // 1: regulation.TrafficRegulation.GetTodayControlLogs:input_type -> regulation.IntersectionRequestForLogs
	2, // 2: regulation.TrafficRegulation.GetLastWeekControlLogs:input_type -> regulation.IntersectionRequestForLogs
	1, // 3: regulation.TrafficRegulation.ReceiveDataForLogs:output_type -> regulation.TrafficDataForLogsReceiveResponse
	3, // 4: regulation.TrafficRegulation.GetTodayControlLogs:output_type -> regulation.TrafficRegulationResponse
	3, // 5: regulation.TrafficRegulation.GetLastWeekControlLogs:output_type -> regulation.TrafficRegulationResponse
	3, // [3:6] is the sub-list for method output_type
	0, // [0:3] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_traffic_regulation_proto_init() }
func file_traffic_regulation_proto_init() {
	if File_traffic_regulation_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_traffic_regulation_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*TrafficDataForLogs); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_traffic_regulation_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*TrafficDataForLogsReceiveResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_traffic_regulation_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*IntersectionRequestForLogs); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_traffic_regulation_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*TrafficRegulationResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_traffic_regulation_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_traffic_regulation_proto_goTypes,
		DependencyIndexes: file_traffic_regulation_proto_depIdxs,
		MessageInfos:      file_traffic_regulation_proto_msgTypes,
	}.Build()
	File_traffic_regulation_proto = out.File
	file_traffic_regulation_proto_rawDesc = nil
	file_traffic_regulation_proto_goTypes = nil
	file_traffic_regulation_proto_depIdxs = nil
}
