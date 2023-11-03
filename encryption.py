key = "ajshgfjasb7y4h3oil3bno8"


def encrypt(plaintext):
    encrypted_data = []
    for i in range(len(plaintext)):
        num = ord(plaintext[i]) ^ ord(key[i % len(key)])
        encrypted_data.append(chr(num))
    return "".join(encrypted_data)


def decrypt(ciphertext):
    decrypted_data = []
    for i in range(len(ciphertext)):
        num = ord(ciphertext[i]) ^ ord(key[i % len(key)])
        decrypted_data.append(chr(num))
    return "".join(decrypted_data)
