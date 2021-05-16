import socket
from utils import get_checksum
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

sock.listen(1)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        res = []
        buffer = 9
        while True:

            data = connection.recv(buffer)
            print('received {!r}'.format(data))

            if data[:3] == b'BLK':
                number_of_words = data[4:]
                buffer = 5
                connection.sendall(bytes(f'RCV-{int(number_of_words)}', 'UTF-8'))

            elif data == b'EOL':
                checksum = get_checksum(res)
                connection.sendall(bytes(f'ACK-{checksum}', 'UTF-8'))
                print(checksum, res)

            elif data:
                print(data)
                try:
                    res.append(int(data))
                except ValueError:
                    print('dip')


            else:
                print('no data from', client_address)
                break

    finally:
        connection.close()