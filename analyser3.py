import pyshark
import socket
import matplotlib.pyplot as plt

def get_ip(packet, dest_adress):
    if 'IP' in packet:
        adress = packet['IP'].dst
        try :
            dest_adress[adress] += 1
        except :
            dest_adress[adress] = 1
def get_domain_or_address(address):
    try:
        return socket.gethostbyaddr(address)[0]
    except socket.herror:
        return address

def plot_top_destinations(destinations, counts):
    keys = [get_domain_or_address(address) for address in destinations]
    values = counts
    plt.pie(values, labels=keys, autopct='%1.1f%%')
    plt.savefig("IP_placing_file_web.jpg", dpi=500)
    plt.show()

def main():
    capture = pyshark.FileCapture("web/placing_file.pcapng")
    Hashmap = {}

    for packet in capture:
        get_ip(packet, Hashmap)

    capture.close()

    eight_best = sorted(Hashmap, key=Hashmap.get, reverse=True)[0:8] 
    counts = [Hashmap[address] for address in eight_best]

    plot_top_destinations(eight_best, counts)

if __name__ == "__main__":
    main()
