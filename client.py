import socket
from utils import get_checksum, get_blocks_sequence, get_number_of_blocks

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

number_of_blocks = get_number_of_blocks()

try:
    words_in_block, words = get_blocks_sequence()
    message = bytes(f'BLK-{words_in_block}', 'UTF-8')
    print('sending {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    # check for RCV-int instead of len(msg)
    amount_expected = len(message)
    i = 1
    while True:
        #words = [87541, 12093, 10911, 12094, 99801]
        data = sock.recv(9)
        #amount_received += len(data)
        print(data, bytes(f'RCV-{words_in_block}', 'UTF-8'))
        if data == bytes(f'RCV-{words_in_block}', 'UTF-8'):
            print('received {!r}'.format(data))

            for word in words:
                sock.sendall(bytes(f'{word}', 'UTF-8'))

            #if number_of_blocks == i:
            sock.sendall(b'EOL')
            #else:
            #    i+=1

        elif data[:3:] == b'ACK':
            print(get_checksum(words), data[4::])
            if bytes(str(get_checksum(words)), 'UTF-8') == data[4::]:
                print('zgadza sie md5')
            else:
                print('nie zgadza się md5')

            break


finally:
    print('closing socket')
    sock.close()

print('elooo')



def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10

    return r



