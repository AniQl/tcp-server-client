import socket
from utils import get_checksum, save_to_file

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

        words_received = []
        buffer = 9
        while True:
            data = connection.recv(buffer)
            # commented out to make STDOUT more readable
            # print('received {!r}'.format(data))

            if data[:3] == b'BLK':
                number_of_words = data[4:]
                # set buffer to 4 as words are 4bytes
                buffer = 4
                connection.sendall(bytes(f'RCV-{int(number_of_words)}', 'UTF-8'))

            elif data == b'ETB':
                checksum = get_checksum(words_received)
                print(f'received ETB, sending checksum: {checksum}')
                connection.sendall(bytes(f'ACK-{checksum}', 'UTF-8'))
                buffer = 9
                save_to_file(words_received, 'server_received_data.txt')
                # clear words_received buffer to be ready for next block
                words_received.clear()

            elif data == b'EOT':
                print('received EOT, stopping server...')
                break

            elif data:
                try:
                    words_received.append(data)

                except ValueError as e:
                    print(f'ERROR: {e} for value: {data} ')

            else:
                print(f'no data from {client_address}, stopping server...')
                break

    finally:
        connection.close()
