#! /bin/bash

curl "https://storage.googleapis.com/gctf-2018-attachments/5a0fad5699f75dee39434cc26587411b948e0574a545ef4157e5bf4700e9d62a" -o letter.zip 2>/dev/null 

unzip -o letter.zip >/dev/null 2>&1

pdftotext challenge.pdf

cat challenge.txt | grep CTF

