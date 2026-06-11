import socket

port=9001
# AF_INET = use IPv4 addresses (e.g. 127.0.0.1)
# SOCK_STREAM = TCP: reliable, ordered, connection-based
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# SO_REUSEADDR lets us restart without waiting for the OS to 
# release the port — saves frustration during development 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Binding: claim port 9000 on the local machine
server_socket.bind(('0.0.0.0', port))

# Begin listening, queue at most 1 waiting connection
server_socket.listen(1)
print(f'Listening on port {port}...')

for i in range(1):
    # accept() blocks here; program pauses until client connects
    client_socket, address = server_socket.accept()
    print(f"{i+1}. Connection from {address}")
    
    # recv(1024): read up to 1024 bytes form the client
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")
    print(len(data))
    
    # sockets send bytes, not strings
    client_socket.sendall(b'Hello from raw socket server!')
    
    # close this connection and return to waiting
    client_socket.close()