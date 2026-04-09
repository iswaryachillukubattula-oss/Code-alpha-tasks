from scapy.all import sniff, IP, Raw

def packet_callback(packet):
    if packet.haslayer(IP):
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)

    print("Protocol:", packet.summary())

    if packet.haslayer(Raw):
        print("Payload:", packet[Raw].load)
sniff(prn=packet_callback, count=10)