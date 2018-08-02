#! /usr/bin/env python

import base64
from Crypto.Cipher import AES

ciphertext = 'rW4q3swEuIOEy8RTIp/DCMdNPtdYopSRXKSLYnX9NQe8z+LMsZ6Mx/x8pwGwofdZ'
key = '6v3TyEgjUcQRnWuIhjdTBA=='

ciphertext = base64.b64decode(ciphertext)
key = base64.b64decode(key)



print ciphertext
print key


aes = AES.new(key, AES.MODE_ECB)
plaintext = aes.decrypt(ciphertext)

print '--- plaintext ---'
print plaintext


