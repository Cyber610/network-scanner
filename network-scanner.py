#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
        print("IP\t\t\tMAC address\n------------------------------------------------")
        for element in answered:
                print(element[1].psrc+"\t\t"+element[1].hwsrc)
scan("YOUR IP ADDRESS OR IP ADDRESS RANGE")
