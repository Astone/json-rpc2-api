#!/usr/bin/env python
from bjsonrpc.handlers import BaseHandler
from bjsonrpc import createserver, bjsonrpc_options
from private import secret_message
import time

class Api(BaseHandler):

    def greeting(self, name, delay=0):
        time.sleep(delay)
        return {'message': secret_message(name)}

if __name__ == '__main__':
    bjsonrpc_options['threaded'] = True
    server = createserver(host='127.0.0.1', port=8080, handler_factory=Api)
    server.debug_socket(True)
    server.serve()
