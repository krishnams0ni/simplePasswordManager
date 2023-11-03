class Encryption:
    def encrypt(s):
        l = list(s)
        l.reverse()
        i = 0
        while i < len(l) - 1:
            l[i], l[i + 1] = l[i + 1], l[i]
            i += 2
        return "".join(l)

    def decrypt(s):
        l = list(s)
        i = 0
        while i < len(l) - 1:
            l[i], l[i + 1] = l[i + 1], l[i]
            i += 2
        l.reverse()
        return "".join(l)


import userOps

dbOps.removeUser()

# original_message = "Hello!"
# encrypted = Encryption.encrypt(original_message)
# decrypted = Encryption.decrypt(encrypted)
# print("Original:", original_message)
# print("Encrypted:", encrypted)
# print("Decrypted:", decrypted)
