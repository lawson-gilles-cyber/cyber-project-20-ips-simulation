# IPS Detection + Response

from core.firewall import block_ip

def analyze_and_block(log):

    # Detect brute force
    if "FAILED LOGIN" in log:
        ip = log.split("-")[-1].strip()
        block_ip(ip)
        return f"[IPS] Blocked IP due to brute force: {ip}"

    # Detect scanning
    if "SCAN" in log:
        ip = log.split("-")[1].strip()
        block_ip(ip)
        return f"[IPS] Blocked IP due to scanning: {ip}"

    return None
