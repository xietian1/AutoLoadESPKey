#Need to run >= Python 3.5


import os
import subprocess
from os.path import expanduser



rnt = subprocess.check_output(["adb", "shell", "su", "-c", "ip xfrm state"])
xfrm_rnt = str(rnt).split("\\r\\n")


for i in range(4):
    #line 0: get src & dst address
    tmp = xfrm_rnt[i*7+0].split(" ")
    src = tmp[1]
    dst = tmp[3]
    #line 1: get spi id
    tmp = xfrm_rnt[i*7+1].split(" ")
    spi = tmp[3]
    #line 3: get auth key
    tmp = xfrm_rnt[i*7+3].split(" ")
    auth_key = tmp[2]
    #line 4: get encrption key
    tmp = xfrm_rnt[i*7+4].split(" ")
    encryption_key = tmp[2]


    #print string directly to terminal
    print('"IPv6","' + src + '","' + dst + '","' + spi + '","AES-CBC [RFC3602]","' + encryption_key + '","HMAC-MD5-96 [RFC2403]","' + auth_key + '"\n')

