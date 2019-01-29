#!/usr/bin/env python3
from binascii import hexlify, unhexlify

encrypted_flag = unhexlify('277f6e7d683e0e526a7c1c3f79395136367e7d67281079613a31106473512c217e3a6d303d3e74')

string_to_encrypt = b'b0ctf{AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA}'

# string_to_encrypt = b'A' # FILL THIS IN
key = b'AAAA' # FILL THIS IN

def encrypt(plaintext, key):
    key = bytes(''.join(str(key)[i % len(key)] for i in range(len(plaintext)+1)), 'utf8')
    result = []
    for i in range(len(plaintext)):
        result.append(key[i] ^ key[i+1] ^ plaintext[i])
    return bytes(result)

def decrypt(ciphertext, key):
    key = bytes(''.join(str(key)[i % len(key)] for i in range(len(ciphertext)+1)), 'utf8')
    result = []
    for i in range(len(ciphertext)):
        result.append(ciphertext[i] ^ key[i] ^ key[i+1])
#        result.append(ciphertext[i] ^ key[i] ^ key[i+1] ^ ciphertext[i] ^ ciphertext[i])
    return bytes(result)

encrypted = encrypt(string_to_encrypt, key)
print('encrypted     : ', encrypted)
print('                ', hexlify(encrypted))
print('encrypted_flag: ', b'277f6e7d683e0e526a7c1c3f79395136367e7d67281079613a31106473512c217e3a6d303d3e74')
decrypted = decrypt(encrypted, key)
print('decrypted     : ', decrypted)
print('                ', hexlify(decrypted))


print('XOR           : ', decrypted^encrypted)

