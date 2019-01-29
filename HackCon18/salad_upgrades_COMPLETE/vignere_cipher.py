#! /usr/bin/env python

import itertools
import string
import collections
from hashlib import sha256

lowercase = collections.deque( string.ascii_lowercase + string.digits )
message = 'e4uo{zo1b_1e_f0j4l10i}z0ce'
key = 'bcdefghijklmnopqrstuvwxyza'


def encrypt( message, key, multipler=-1 ):
	compressed_message = message.lower()

	cycler = itertools.cycle(key.lower())
	long_key = ''.join( [ cycler.next() for _ in range(len(compressed_message)) ] )

	coded = []
	
	for number in range(len(long_key)):
		try:
			cipher_letter = compressed_message[number]
			key_letter = long_key[number]
			key_index = string.ascii_lowercase.index(key_letter)
			cipher_index = string.ascii_lowercase.index(cipher_letter)

			lowercase = collections.deque( string.ascii_lowercase )
			lowercase.rotate( multipler * key_index )
			new_alphabet = ''.join(list(lowercase))
			new_character = new_alphabet[cipher_index]
			coded.append( new_character )
		except:
			coded.append( compressed_message[number] )

	return ''.join(coded)

def decrypt( message, key, multipler=-1 ):
	return encrypt( message, key, 1)

print decrypt(message, key)

