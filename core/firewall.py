# Firewall simulation (blocking IPs)

def block_ip(ip):

    # Save blocked IP to file
    with open("blocked/blocked_ips.txt", "a") as file:
        file.write(ip + "\n")
