#Need to run >= Python 3.5

import os
import subprocess
from os.path import expanduser


home = expanduser("~")

_set = set()
readfile = open(home+'/.config/wireshark/esp_sa', 'r')
for line in readfile:
    tmp = line.split(',')
    if len(tmp) > 2:
    	_set.add(tmp[3][1:-1]) #add existing to hashset
readfile.close()

print("Existing SA key: " + str(len(_set)))

loadfile = open('esp_key', 'r')
myfile = open(home+'/.config/wireshark/esp_sa', 'a')

for i in range(4):
    #line 0: get src & dst address
    tmp = loadfile.readline().strip().split(" ")
    #tmp = xfrm_rnt[i*7+0].split(" ")
    src = tmp[1]
    dst = tmp[3]
    #line 1: get spi id
    tmp = loadfile.readline().strip().split(" ")
    spi = tmp[3]
    #line 2
    loadfile.readline()
    #line 3: get auth key
    tmp = loadfile.readline().strip().split(" ")
    auth_key = tmp[2]
    #line 4: get encrption key
    tmp = loadfile.readline().strip().split(" ")
    encryption_key = tmp[2]
    #line 5:
    loadfile.readline()
    #line 6:
    loadfile.readline()
    if spi not in _set:
        myfile.write('"IPv6","' + src + '","' + dst + '","' + spi + '","AES-CBC [RFC3602]","' + encryption_key + '","HMAC-MD5-96 [RFC2403]","'+ auth_key + '"\n')
        print("load one!" + spi)
    else:
        print("SPI:" + spi + " already exists")
    
myfile.close()




