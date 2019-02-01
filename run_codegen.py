from grpc_tools import protoc

protoc.main((
    '',
    '-I./podder_task_base/api/',
    '--python_out=.',
    '--grpc_python_out=./',
    './podder_task_base/api/protos/pipeline_framework.proto',
))
