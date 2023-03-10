#!/usr/bin/env python3
import random
from typing import Optional

import grpc
import sum_pb2 as pb2
import sum_pb2_grpc as pb2_grpc


class SumClient:
    """
    Client for gRPC functionality
    """

    def __init__(self, uri: str = '127.0.0.1', port: int = 50051) -> None:
        # instantiate a channel
        self.channel = grpc.insecure_channel(f'{uri}:{port}')
        # bind the client and the server
        self.stub = pb2_grpc.SumServiceStub(self.channel)

    def get_url(self, a, b):
        """
        Client function to call the rpc for Sum
        """
        result = pb2.SumRequest(a=a, b=b)
        return self.stub.Sum(result)

    def __call__(self, *, a: Optional[int] = None, b: Optional[int] = None) -> int:
        a = random.randint(1, 1000) if a is None else a
        b = random.randint(1, 1000) if b is None else b
        result = self.get_url(a=a, b=b)
        c = result.result
        assert a + b == c, 'Wrong sum'
        return c