#! /bin/bash

echo 'YWRtaW46dW5pY29ybmlj' | base64 -d | cut -d ':' -f2 
