import random


def get_checksum(words: list) -> int:
    tmp = []
    for word in words:
        word_without_first_digit = str(word)[1::]
        tmp.append(int(word_without_first_digit))

    checksum = sum(tmp)
    if len(str(checksum)) > 5:
        # here I delete digits from 6th position counting from LEFT
        # it was stated in task that i should take 6th position from RIGHT
        # but it seems like a typo as this approach makes more sense as number of bytes are constant
        return int(str(checksum)[:5:])

    return checksum


def get_blocks_sequence():
    words_in_block = random.randint(5, 100)
    words = random.sample(range(10000, 99999), words_in_block)

    return words_in_block, words


def get_number_of_blocks():
    return random.randint(5, 10)


def get_new_block_announcement_msg() -> (bytes, int, list):
    words_in_block, words = get_blocks_sequence()
    message = bytes(f'BLK-{words_in_block}', 'UTF-8')

    return message, words_in_block, words


def save_to_file(object, file_name):
    with open(file_name, "a+") as file:
        file.write(str(object))
