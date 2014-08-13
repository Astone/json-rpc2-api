#!/usr/bin/env python
from tornadorpc import async
from threading import Thread
from tornadorpc import start_server
from tornadorpc.json import JSONRPCHandler
from private import secret_message
import time

class ServerAgentAsync(Thread):

    def __init__(self, method, callback, *args, **kwargs):
        super(ServerAgentAsync, self).__init__()
        self.method = getattr(self, method)
        self.callback = callback
        self.kwargs = kwargs

    def run(self):
        try:
            self.callback(self.method(**self.kwargs))
        except Exception as err:
            self.callback(err)

    def greeting(self, name, delay=0):
        time.sleep(delay)
        return {'message': secret_message(name)}

class ServerAgentApi(JSONRPCHandler):

    @async
    def greeting(self, *args, **kwargs):
        agent = ServerAgentAsync("greeting", self.result, *args, **kwargs)
        agent.start()

if __name__ == '__main__':
    start_server(ServerAgentApi, port=8080)
