#! /bin/bash
zbarimg solved.bmp | cut -d ':' -f2 | tac | tr -d '\n'
echo ''


