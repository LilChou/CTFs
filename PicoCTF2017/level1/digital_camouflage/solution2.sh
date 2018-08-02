#! /bin/bash

strings data.pcap | grep pswrd | cut -d '=' -f3 | tail -n 1 | while read line; do echo ${line//\%3D/=}; done | base64 -d

