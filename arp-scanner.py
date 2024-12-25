import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ethernet(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)
    
    print("Aktiv Hostlar:")
    for element in answered:
        print(f"IP: {element[1].psrc} | MAC: {element[1].hwsrc}")

ip = input("Zəhmət olmasa skan etmək istədiyiniz IP ünvanını daxil edin: ")
scan(ip)
