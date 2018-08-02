#! /bin/bash
strings hacker.jpg | tail -n 1 | base64 -d | cut -d ' ' -f3
