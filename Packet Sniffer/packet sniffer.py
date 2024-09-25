!pip install scapy matplotlib


from scapy.all import sniff

# Lists to store packet sizes and timestamps
packet_sizes = []
timestamps = []

#Handle packets and get the necessary data
def packet_handler(packet):
  print(packet)
  packet_sizes.append(len(packet))
  timestamps.append(packet.time)

# Start packet sniffing on the default network interface
sniff(prn = packet_handler , count=100)


import matplotlib.pyplot as plt

# Create a plot
plt.figure(figsize=(16,8))
plt.plot(timestamps, packet_sizes, marker='o')
plt.xlabel("Time")
plt.ylabel("Packet Size")
plt.title("Packet Size over Time")
plt.grid(True)
plt.show()
