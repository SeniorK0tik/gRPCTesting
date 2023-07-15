import pytest
import grpc

from src import myservice_pb2_grpc
from src.myservice_pb2_grpc import MyServiceStub


@pytest.fixture(scope="session")
def grpc_client() -> MyServiceStub:
    channel = grpc.insecure_channel('localhost:50051')
    client = myservice_pb2_grpc.MyServiceStub(channel)
    return client