import socket
from utils import get_checksum, get_number_of_blocks, get_new_block_announcement_msg, save_to_file

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

number_of_blocks = get_number_of_blocks()

try:
    message, words_in_block, words = get_new_block_announcement_msg()
    print('sending {!r}'.format(message))
    sock.sendall(message)
    i = 1
    while True:
        data = sock.recv(9)
        if data == bytes(f'RCV-{words_in_block}', 'UTF-8'):
            print('received {!r}'.format(data))

            for word in words:
                sock.sendall(bytes(f'{word}', 'UTF-8'))

            save_to_file(words, 'client_received_data.txt')
            sock.sendall(b'ETB')

        elif data[:3:] == b'ACK':
            if bytes(str(get_checksum(words)), 'UTF-8') == data[4::]:
                print('received checksum == internal checksum')
                if number_of_blocks == i:
                    sock.sendall(b'EOT')
                    break
                else:
                    i += 1
                    message, words_in_block, words = get_new_block_announcement_msg()
                    print('sending {!r}'.format(message))
                    sock.sendall(message)
            else:
                print('received checksum != internal checksum')
                print('transmission error, closing connection')
                break

finally:
    print('closing socket')
    sock.close()
