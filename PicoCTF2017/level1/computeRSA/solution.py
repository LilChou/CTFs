#! /usr/bin/env python

ciphertext = 150815
d = 1941
N = 435979

plaintext = ciphertext ** d % N
print plaintext
