import socket

from contextlib import contextmanager

@contextmanager
def socket_server_TCP(port, host):
    try:
        print("Opening a connection (TCP)")
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(1)
        yield server
    except:
        print("No connection established. The port may already be in use ")
    finally:
        print("Closing a connection (TCP)")
        server.close()

@contextmanager
def socket_server_UDP(host, port):
    try:
        print("Opening a connection (UDP)")
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.bind((host, port))
        yield server
    except:
        print("No connection established. The port may already be in use ")
    finally:
        print("Closing a connection (UDP)")
        server.close()


with socket_server_TCP(host="127.0.0.1", port=8081) as server:
    client_socket, address = server.accept()
    print('Accepted connection from {}:{}'.format(address[0], address[1]))
    request = client_socket.recv(1024)
    print('Received {}'.format(request))
    client_socket.send('ACK!'.encode())
    client_socket.close()

with socket_server_UDP(host="127.0.0.1", port=8082) as server:
    print('wait data...')
    request, address = server.recvfrom(1024)
    print('Accepted connection from {}:{}'.format(address[0], address[1]))
    print('Received {}'.format(request))
    server.sendto(b'message received by the server: ' + request, address)




