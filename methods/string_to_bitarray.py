def string_to_bitarray(message):
    bitarray = []
    for character in message:
        bit = int(character)
        bitarray.append(bit)

    return bitarray
