def encrypt_message(message_bits, one_time_pad_bits):
    encrypt = []

    for i in range(len(message_bits)):
        bit = message_bits[i] ^ one_time_pad_bits[i]
        encrypt.append(bit)

    return encrypt
