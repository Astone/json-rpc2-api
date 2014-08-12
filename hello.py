from private import secret_message

def greeting(name):
    return {'message': secret_message(name)}
