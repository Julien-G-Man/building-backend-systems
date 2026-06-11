import socket

def parse_request(raw: bytes) -> dict:
    text = raw.decode('utf-8', errors='replace')
    lines = text.split('\r\n')
    parts = lines[0].split(' ')
    return {'method': parts[0] if len(parts) > 0 else '',
            'path':   parts[1] if len(parts) > 1 else '/'}
    

def make_response(status: int, body: str) -> bytes:
    reason = {200: 'OK', 404:'Not Found', 405:'Method Not Allowed'}.get(status, 'Unknown')
    return (
        f'HTTP/1.1 {status} {reason}\r\n'
        f'Content-Type: application/json\r\n'
        f'Content-Length: {len(body.encode())}\r\n'
        f'Connection: close\r\n'
        f'\r\n'
        f'{body}'
    ).encode()
    

ROUTES = {
    ('GET',  '/'):      (200, '{"message": "Welcome"}'),
    ('GET', '/health'): (200, '{"status": "ok"}'),
    ('POST', '/echo'): (200, '{"echo": "received"}')
}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
server.bind(('127.0.0.1', 9000))
server.listen(5)
print('HTTP server listening on http://127.0.0.1:9000')

while True:
    client, addr = server.accept()
    raw = client.recv(4096)
    req = parse_request(raw)
    key = (req['method'], req['path'])
    status, body_str = ROUTES.get(key, (404, '{"error": "Not found"}'))
    response = make_response(status, body_str)
    print(response)
    client.sendall(response)
    client.close()