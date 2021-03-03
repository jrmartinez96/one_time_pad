from methods.string_to_bits import string_to_bits
from methods.generate_one_time_pad import generate_one_time_pad
from methods.encrypt_message import encrypt_message
from methods.bitarray_to_string import bitarray_to_string


def encrypt():
    message = input("Ingresa el texto a encriptar: ")

    # Manejo de bits
    message_bits = string_to_bits(message)
    one_time_pad = generate_one_time_pad(message_bits)
    message_encrypted = encrypt_message(message_bits, one_time_pad)

    # Bitarrays a string
    message_encrypted_file_text = bitarray_to_string(message_encrypted)
    one_time_pad_file_text = bitarray_to_string(one_time_pad)

    # Escritura de archivos
    message_encrypted_file = open("me.txt", "w")
    message_encrypted_file.write(message_encrypted_file_text)
    message_encrypted_file.close()

    one_time_pad_file = open("otp.txt", "w")
    one_time_pad_file.write(one_time_pad_file_text)
    one_time_pad_file.close()


encrypt()
