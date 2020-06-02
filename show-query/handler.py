import os

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    print('Request type: {}'.format(type(req)))
    print('Request length: {}'.format(len(req)))
    print('Request: {}'.format(req))
    print('Environment:')
    for k,v in os.environ.items():
        print('    {}: {}'.format(k,v))
