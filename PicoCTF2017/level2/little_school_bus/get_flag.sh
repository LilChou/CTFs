#! /bin/bash
zsteg littleschoolbus.bmp | grep flag | cut -d '"' -f2 
