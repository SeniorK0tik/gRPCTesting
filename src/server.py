import time
from concurrent import futures
import random

import grpc

from src import myservice_pb2_grpc, myservice_pb2


class Events:
    def __call__(self):
        return f"Event {random.randint(1, 100)}"

class MyServiceServicer(myservice_pb2_grpc.MyServiceServicer):
    def __init__(self):
        self.event = Events()

    def GetRandomEvent(self, request, context):
        return myservice_pb2.EventResponse(event=self.event())

def start():
    server = grpc.server(futures.ThreadPoolExecutor())
    myservice_pb2_grpc.add_MyServiceServicer_to_server(MyServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('SERVER IS LISTENING')

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
