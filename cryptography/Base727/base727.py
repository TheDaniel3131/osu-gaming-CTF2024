import binascii


def decode_base_727(encoded_string):
    base = 727
    decoded_value = 0

    for char in encoded_string:
        decoded_value = decoded_value * base + ord(char)

    decoded_string = ""

    while decoded_value > 0:
        decoded_string = chr(decoded_value % 256) + decoded_string
        decoded_value //= 256

    return decoded_string


encoded_string_hex = b'06c3abc49dc4b443ca9d65c8b0c386c4b0c99fc798c2bdc5bccb94c68c37c296ca9ac29ac790c4af7bc585c59d'
encoded_string = binascii.unhexlify(encoded_string_hex).decode()

decoded_string = decode_base_727(encoded_string)
print(decoded_string)
