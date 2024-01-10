import socket
from views import *

URLS = {
    '/': index,
    '/blog': blog,
    '/about': about,
    '/contact': contact,
    '/404': not_found,
    '/405': method_not_allowed
}


def generate_headers(method, url) -> tuple:
    """
    Generate headers dict based on request method and url
    """
    if not method == 'GET':
        raise NotImplementedError("Only GET method is supported")

    if not url.startswith('/'):
        raise ValueError("URL must start with /")

    if not url.endswith('/') and not method == 'GET':
        raise ValueError("URL must end with /")
    
    if url not in URLS:
        return ('HTTP/1.1 404 Not found\n\n', 404)

    if url == '/':
        url = '/index.html'

    return ('HTTP/1.1 200 OK\n\n', 200)

def generate_content(code, url) -> str:

    if code == 404:
        return URLS['/404']()
    
    if code == 405:
        return URLS['/405']()
        
    return URLS[url]()

def generate_response(request) -> tuple:
    """
    Generate a response to the client's request
    """
    method, url = request.split(' ')[:2]
    header, code = generate_headers(method, url)
    body = generate_content(code, url)

    return (header + body).encode(), code


def run():
    """
    socket.AF_INET is for ipv4
    socket.SOCK_STREAM is for TCP

    socket.SOL_SOCKET is for socket level
    socket.SO_REUSEADDR is for reusing the socket (all of this staff helps to avoid the error: OSError: [Errno 48] Address already in use)
    """
    print("Starting socket server...")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        client_socket, address = server_socket.accept()
        print("Connection from {address} has been established.".format(address=address))
        request = client_socket.recv(1024)
        print("Request: {request}".format(request=request))

        response = generate_response(request.decode('utf-8'))

        client_socket.sendall(response[0])
        client_socket.close()

if __name__ == '__main__':
    run()