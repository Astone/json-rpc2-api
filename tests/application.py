#!/usr/bin/env python
from jsonrpclib import Server
from threading import Thread
import time


class ServerAgent():

    URL = "http://localhost:8080"

    def __init__(self):
        self.api = Server(self.URL)
        self.actions = []

    def call_async(self, method, **kwargs):
        method = getattr(self.api, method)
        action = ServerAgent.Action(method, **kwargs)
        action.start()
        self.actions.append(action)
        return action

    def call(self, method, **kwargs):
        action = self.call_async(method, **kwargs)
        action.join()
        return action.get_result()

    class Action (Thread):

        def __init__(self, method, **kwargs):
            super(ServerAgent.Action, self).__init__()
            self.method = method
            self.kwargs = kwargs
            self.result = None
            self.error = None

        def run(self):
            try:
                self.result = self.method(**self.kwargs)
            except Exception as err:
                self.error = err

        def get_result(self):
            if self.isAlive():
                return None
            if self.error:
                return self.error
            return self.result

if __name__ == '__main__':

    api = ServerAgent()
    act1 = api.call_async("greeting", name="First Person", delay=5)
    act2 = api.call_async("greeting", name="Second Person", delay=2)

    for i in range(10):
        print i+1, act1.get_result(), act2.get_result()
        time.sleep(1)
