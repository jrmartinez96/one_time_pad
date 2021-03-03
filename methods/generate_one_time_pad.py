import random


def generate_one_time_pad(message_bits):
    one_time_pad = []

    for message_bit in message_bits:
        bit = random.randint(0, 1)
        one_time_pad.append(bit)

    return one_time_pad