#! /bin/bash

for i in {1..26}; do cat enc.txt | caesar $i; done;

