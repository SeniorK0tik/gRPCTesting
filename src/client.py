import time

import grpc

from src import myservice_pb2_grpc, myservice_pb2


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = myservice_pb2_grpc.MyServiceStub(channel)

    try:
        while True:
            response = stub.GetRandomEvent(myservice_pb2.Empty())
            yield response.event
            # print("Received event:", response.event)
            time.sleep(1)
    except KeyboardInterrupt:
        pass

def get_response(event: str):
    print(event)


if __name__ == '__main__':
    run()