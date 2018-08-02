#! /bin/bash

cat found_chat.txt | rev | cut -d ' ' -f1 | rev | tr -d '\n' 
