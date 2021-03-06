import time
import signal
from concurrent import futures
from typing import Any, Optional
import grpc


class GrpcServer(object):
    def __init__(self, stdout_file: str, stderr_file: str, execution_task: Any,
                 max_workers: int, max_rpcs_requests: Optional[str],
                 port: int, add_servicer_method: Any, task_api_class: Any):
        self.stdout_file = stdout_file
        self.stderr_file = stderr_file
        self.execution_task = execution_task
        self.max_workers = max_workers
        self.max_rpcs_requests = max_rpcs_requests
        self.port = port
        self.add_servicer_to_server = add_servicer_method
        self.task_api_class = task_api_class

    def run(self):
        max_requests = int(self.max_rpcs_requests) if self.max_rpcs_requests else None

        server_options = [
            # send keepalive ping every 1 second. default: 2 hours
            ('grpc.keepalive_time_ms', 1000),
            # keepalive ping time out. default: 20 seconds
            ('grpc.keepalive_timeout_ms', 1000),
            ('grpc.keepalive_permit_without_calls', True),
            ('grpc.http2.max_pings_without_data', 0),
            # allow grpc ping from client every 1 second
            ('grpc.http2.min_time_between_pings_ms', 1000),
            # allow grpc ping from client without data every 1 second
            ('grpc.http2.min_ping_interval_without_data_ms', 1000),
        ]

        print('gRPC server options: {}'.format(server_options))
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=int(self.max_workers)),
                             options=server_options,
                             maximum_concurrent_rpcs=max_requests)
        self.add_servicer_to_server(self.task_api_class(self.execution_task), server)
        server.add_insecure_port('[::]:' + str(self.port))
        server.start()

        print("[{}] gRPC server is listening to port: '[::]:{}'".format(
            time.strftime("%Y-%m-%d %H:%m:%S"), self.port))

        # stop gRPC server when SIGTERM signal received
        def sigterm_handler(signum, frame):
            print("SIGTERM received.")
            server.stop(0)
        signal.signal(signal.SIGTERM, sigterm_handler)

        try:
            server.wait_for_termination()
        except KeyboardInterrupt:
            print("SIGINT received.")
            server.stop(0)

        print("stopped gRPC server.")
