#! /usr/bin/env python

from pwn import *
import struct

print p32(0xcaf3baee)

print struct.pack('<I', 0xcaf3baee)

