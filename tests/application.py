#!/usr/bin/env python
from bjsonrpc import connect
import time

api = connect(host='localhost', port=8080)
req1 = api.method.greeting(name="First Person", delay=5)
req2 = api.method.greeting(name="Second Person", delay=2)

for i in range(10):
    time.sleep(1)
    print i+1,
    if req1.hasresponse():
        print req1.value.get('message'),
        req1.setresponse(None)
    if req2.hasresponse():
        print req2.value.get('message'),
        req2.setresponse(None)
    print
