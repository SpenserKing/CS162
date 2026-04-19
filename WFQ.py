
premium = []
standard = []
economy = []

# Given stream
packets = [
    "S Mary",
    "P Dee",
    "P Dee",
    "E Eileen",
    "E Mike",
    "E Joe",
    "P Dee",
    "E Vicky",
    "E George",
    "P Dee",
    "P Joe",
    "E Sally",
    "P Joe",
    "S Pete",
    "P Dee",
    "S Bill",
    "S Chase",
    "E Price",
    "P Dee",
    "E Sue"]

# Building queues
for packet in packets:
    priority = packet[0]

    if priority == "P":
        premium.append(packet)
    elif priority == "S":
        standard.append(packet)
    elif priority == "E":
        economy.append(packet)

# Printing starting queues
print("Premium Queue:", premium)
print("Standard Queue:", standard)
print("Economy Queue:", economy)
print("\nDequeued output in WFQ order:")

# Applying weighted fair queuing
while premium or standard or economy:

    # Print up to 3 Premium packets
    for _ in range(3):
        if premium:
            print(premium.pop(0))
    # Print up to 2 Standard packets
    for _ in range(2):
        if standard:
            print(standard.pop(0))

    # Print up to 1 Economy packet
    for _ in range(1):
        if economy:
            print(economy.pop(0))