import pytest

from src import myservice_pb2


@pytest.fixture()
def get_random_event(grpc_client):
    return grpc_client.GetRandomEvent(myservice_pb2.Empty())