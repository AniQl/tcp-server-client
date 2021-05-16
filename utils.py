import random


def get_checksum(words):
    tmp = []
    for word in words:
        word_without_first_digit = str(word)[1::]
        tmp.append(int(word_without_first_digit))

    checksum = sum(tmp)
    if len(str(checksum)) > 5:
        return int(str(checksum)[:5:])

    return checksum


def get_blocks_sequence():
    # blocks_number = random.randint(5, 10)
    words_in_block = random.randint(5, 100)
    words = random.sample(range(10000, 99999), words_in_block)

    return words_in_block, words


def get_number_of_blocks():
    return random.randint(5, 10)
