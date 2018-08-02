#! /bin/bash

curl "http://ctf.ryanic.com:8080/secret.html" 2>/dev/null | grep FLAG | cut -d ' ' -f3

