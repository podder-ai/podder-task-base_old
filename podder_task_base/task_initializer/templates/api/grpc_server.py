"""
DO NOT MODIFY THIS FILE.
"""

import os

from api.task_api import PodderTaskApi
from app import Task
from podder_task_base.api.grpc_server import GrpcServer
from protos import pipeline_framework_pb2_grpc

DEFAULT_PORT = 50051
DEFAULT_MAX_WORKERS = 10

if __name__ == '__main__':
    """
    Run gRPC server.
    """
    GrpcServer(
        stdout_file=open(os.getenv("GRPC_LOG"), 'a'),
        stderr_file=open(os.getenv("GRPC_ERROR_LOG"), 'a'),
        pidfile_path=os.getenv("GRPC_PID_FILE", "/var/run/poc_base.pid"),
        max_workers=os.getenv("GRPC_MAX_WORKERS", DEFAULT_MAX_WORKERS),
        port=os.getenv("GRPC_PORT", DEFAULT_PORT),
        execution_task=Task,
        add_servicer_method=pipeline_framework_pb2_grpc.add_PodderTaskApiServicer_to_server,
        task_api_class=PodderTaskApi).run()
