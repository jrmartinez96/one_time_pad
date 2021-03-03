from methods.bits_to_string import bits_to_string
from methods.encrypt_message import encrypt_message
from methods.string_to_bitarray import string_to_bitarray
import sys


def decrypt(message_file_name, one_time_pad_file_name):
    # Leer archivos
    message_encrypted_file = open(message_file_name, "r")
    message_encrypted_file_text = message_encrypted_file.read()
    message_encrypted = string_to_bitarray(message_encrypted_file_text)

    one_time_pad_file = open(one_time_pad_file_name, "r")
    one_time_pad_file_text = one_time_pad_file.read()
    one_time_pad = string_to_bitarray(one_time_pad_file_text)

    # Desencriptar
    message_decrypted = encrypt_message(message_encrypted, one_time_pad)
    message_reversed = bits_to_string(message_decrypted)

    print(message_reversed)
    return message_reversed


args = sys.argv
if len(args) == 3:
    decrypt(args[1], args[2])
