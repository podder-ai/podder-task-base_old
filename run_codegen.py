from grpc_tools import protoc

protoc.main((
    '',
    '-I./podder_task_base/api/protos',
    '--python_out=./podder_task_base/api',
    '--grpc_python_out=./podder_task_base/api',
    './podder_task_base/api/protos/pipeline_framework.proto',
))
