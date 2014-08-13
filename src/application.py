import time
from private import secret_message

def greeting(name, delay):
    time.sleep(delay)
    return {'message': secret_message(name)}
