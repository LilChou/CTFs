#! /bin/bash


strings ftp.pcap | grep -i flag | tail -n 1 | cut -d '-' -f2

