import scapy.all as scapy
#İlk öncə scapy kitabxanasını yükləməliyik. (readme.md ni oxuyun)

def scan(ip): #Daxil edəcəyimiz ip addressləri üçün belə bir funksiya yaradırıq
    arp_request = scapy.ARP(pdst=ip) #pdst=ip: Skan olunaca ip ünvanını göstərir
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff') #Ether etherneti ifadə edir, dst='ff:ff:ff:ff:ff:ff' isə broadcast addressidir
    arp_request_broadcast = broadcast/arp_request #Broadcast və arp requesti birləşdirir
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1) #timeout 1 saniyə gözləməsini ifadə edir
    
    print("Aktiv Hostlar:")
    for element in answered: # Bizə cavab verən requestlər lazım olduqu üçün answered-dən istifadə edirik
        print(f"IP: {element[1].psrc} | MAC: {element[1].hwsrc}") #Sorğuya cavab verən ip və mac addresslərini çap edir

ip = input("Zəhmət olmasa skan etmək istədiyiniz IP ünvanını daxil edin: ")
scan(ip)
