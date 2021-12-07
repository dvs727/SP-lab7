import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto('hello world'.encode(), (("localhost", 8082)))
    data, _ = client.recvfrom(1024)
    print(data.decode())
    client.close()

if __name__ == '__main__':
    main()



