import re

import allure

from src.myservice_pb2_grpc import MyServiceServicer
from utils.assertions.grpc.grpc_objects import assert_grpc_example


@allure.title('Get simple gRPC response from server')
def test_get_random_event(get_random_event: MyServiceServicer):
    allure.dynamic.description('5 iterations to check')
    for i in range(5):
        assert_grpc_example(
            expected_text='String starting with string "Event"',
            actual_text=get_random_event.event,
            regex=re.compile("^Event\s\d+$")
        )
