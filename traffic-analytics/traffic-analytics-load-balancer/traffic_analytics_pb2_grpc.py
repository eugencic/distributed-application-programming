# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import traffic_analytics_pb2 as traffic__analytics__pb2


class TrafficAnalyticsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReceiveDataForAnalytics = channel.unary_unary(
                '/analytics.TrafficAnalytics/ReceiveDataForAnalytics',
                request_serializer=traffic__analytics__pb2.TrafficDataForAnalytics.SerializeToString,
                response_deserializer=traffic__analytics__pb2.TrafficDataForAnalyticsReceiveResponse.FromString,
                )
        self.AddDataAnalytics = channel.unary_unary(
                '/analytics.TrafficAnalytics/AddDataAnalytics',
                request_serializer=traffic__analytics__pb2.AddDataAnalyticsRequest.SerializeToString,
                response_deserializer=traffic__analytics__pb2.AddDataAnalyticsResponse.FromString,
                )
        self.DeleteDataAnalytics = channel.unary_unary(
                '/analytics.TrafficAnalytics/DeleteDataAnalytics',
                request_serializer=traffic__analytics__pb2.DeleteDataAnalyticsRequest.SerializeToString,
                response_deserializer=traffic__analytics__pb2.DeleteDataAnalyticsResponse.FromString,
                )
        self.GetTodayStatistics = channel.unary_unary(
                '/analytics.TrafficAnalytics/GetTodayStatistics',
                request_serializer=traffic__analytics__pb2.IntersectionRequestForAnalytics.SerializeToString,
                response_deserializer=traffic__analytics__pb2.TrafficAnalyticsResponse.FromString,
                )
        self.GetLastWeekStatistics = channel.unary_unary(
                '/analytics.TrafficAnalytics/GetLastWeekStatistics',
                request_serializer=traffic__analytics__pb2.IntersectionRequestForAnalytics.SerializeToString,
                response_deserializer=traffic__analytics__pb2.TrafficAnalyticsResponse.FromString,
                )
        self.GetNextWeekPredictions = channel.unary_unary(
                '/analytics.TrafficAnalytics/GetNextWeekPredictions',
                request_serializer=traffic__analytics__pb2.IntersectionRequestForAnalytics.SerializeToString,
                response_deserializer=traffic__analytics__pb2.TrafficAnalyticsResponse.FromString,
                )
        self.TrafficAnalyticsServiceStatus = channel.unary_unary(
                '/analytics.TrafficAnalytics/TrafficAnalyticsServiceStatus',
                request_serializer=traffic__analytics__pb2.TrafficAnalyticsServiceStatusRequest.SerializeToString,
                response_deserializer=traffic__analytics__pb2.TrafficAnalyticsServiceStatusResponse.FromString,
                )


class TrafficAnalyticsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ReceiveDataForAnalytics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddDataAnalytics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteDataAnalytics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTodayStatistics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLastWeekStatistics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNextWeekPredictions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TrafficAnalyticsServiceStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TrafficAnalyticsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReceiveDataForAnalytics': grpc.unary_unary_rpc_method_handler(
                    servicer.ReceiveDataForAnalytics,
                    request_deserializer=traffic__analytics__pb2.TrafficDataForAnalytics.FromString,
                    response_serializer=traffic__analytics__pb2.TrafficDataForAnalyticsReceiveResponse.SerializeToString,
            ),
            'AddDataAnalytics': grpc.unary_unary_rpc_method_handler(
                    servicer.AddDataAnalytics,
                    request_deserializer=traffic__analytics__pb2.AddDataAnalyticsRequest.FromString,
                    response_serializer=traffic__analytics__pb2.AddDataAnalyticsResponse.SerializeToString,
            ),
            'DeleteDataAnalytics': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteDataAnalytics,
                    request_deserializer=traffic__analytics__pb2.DeleteDataAnalyticsRequest.FromString,
                    response_serializer=traffic__analytics__pb2.DeleteDataAnalyticsResponse.SerializeToString,
            ),
            'GetTodayStatistics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTodayStatistics,
                    request_deserializer=traffic__analytics__pb2.IntersectionRequestForAnalytics.FromString,
                    response_serializer=traffic__analytics__pb2.TrafficAnalyticsResponse.SerializeToString,
            ),
            'GetLastWeekStatistics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLastWeekStatistics,
                    request_deserializer=traffic__analytics__pb2.IntersectionRequestForAnalytics.FromString,
                    response_serializer=traffic__analytics__pb2.TrafficAnalyticsResponse.SerializeToString,
            ),
            'GetNextWeekPredictions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNextWeekPredictions,
                    request_deserializer=traffic__analytics__pb2.IntersectionRequestForAnalytics.FromString,
                    response_serializer=traffic__analytics__pb2.TrafficAnalyticsResponse.SerializeToString,
            ),
            'TrafficAnalyticsServiceStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.TrafficAnalyticsServiceStatus,
                    request_deserializer=traffic__analytics__pb2.TrafficAnalyticsServiceStatusRequest.FromString,
                    response_serializer=traffic__analytics__pb2.TrafficAnalyticsServiceStatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'analytics.TrafficAnalytics', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TrafficAnalytics(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ReceiveDataForAnalytics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/analytics.TrafficAnalytics/ReceiveDataForAnalytics',
            traffic__analytics__pb2.TrafficDataForAnalytics.SerializeToString,
            traffic__analytics__pb2.TrafficDataForAnalyticsReceiveResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddDataAnalytics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/analytics.TrafficAnalytics/AddDataAnalytics',
            traffic__analytics__pb2.AddDataAnalyticsRequest.SerializeToString,
            traffic__analytics__pb2.AddDataAnalyticsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteDataAnalytics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/analytics.TrafficAnalytics/DeleteDataAnalytics',
            traffic__analytics__pb2.DeleteDataAnalyticsRequest.SerializeToString,
            traffic__analytics__pb2.DeleteDataAnalyticsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTodayStatistics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/analytics.TrafficAnalytics/GetTodayStatistics',
            traffic__analytics__pb2.IntersectionRequestForAnalytics.SerializeToString,
            traffic__analytics__pb2.TrafficAnalyticsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLastWeekStatistics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/analytics.TrafficAnalytics/GetLastWeekStatistics',
            traffic__analytics__pb2.IntersectionRequestForAnalytics.SerializeToString,
            traffic__analytics__pb2.TrafficAnalyticsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNextWeekPredictions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/analytics.TrafficAnalytics/GetNextWeekPredictions',
            traffic__analytics__pb2.IntersectionRequestForAnalytics.SerializeToString,
            traffic__analytics__pb2.TrafficAnalyticsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TrafficAnalyticsServiceStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/analytics.TrafficAnalytics/TrafficAnalyticsServiceStatus',
            traffic__analytics__pb2.TrafficAnalyticsServiceStatusRequest.SerializeToString,
            traffic__analytics__pb2.TrafficAnalyticsServiceStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
