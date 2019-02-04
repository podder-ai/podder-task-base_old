import os
import time
from concurrent import futures
from typing import Any

import daemon
import grpc
from daemon import pidfile

from podder_task_base.api.task_api import PocBaseApi
from protos import pipeline_framework_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
DEFAULT_MAX_WORKERS = 10
DEFAULT_PORT = 50051


def run_grpc_server(stdout_file: str, stderr_file: str, pidfile_path: str, task_class: Any):
    """
    Run gRPC server with new daemon process.
    """
    pid_lock_file = pidfile.PIDLockFile(pidfile_path)
    with daemon.DaemonContext(
            stdout=stdout_file, stderr=stderr_file, pidfile=pid_lock_file,
            detach_process=True):
        serve(execution_task=task_class)


def serve(execution_task):
    max_workers = os.environ.get("GRPC_MAX_WORKERS") if os.environ.get(
        "GRPC_MAX_WORKERS") else DEFAULT_MAX_WORKERS
    port = os.environ.get("GRPC_PORT") if os.environ.get(
        "GRPC_PORT") else DEFAULT_PORT

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=int(max_workers)))
    pipeline_framework_pb2_grpc.add_PocBaseApiServicer_to_server(
        PocBaseApi(execution_task), server)
    server.add_insecure_port('[::]:' + str(port))

    server.start()
    print("[{}] gRPC server is listening to port: '[::]:{}'".format(
        time.strftime("%Y-%m-%d %H:%m:%S"), port))
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
