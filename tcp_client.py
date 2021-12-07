import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 8081))
    client.send('hello world'.encode())
    response = client.recv(4096)
    print(response)

if __name__ == '__main__':
    main()
