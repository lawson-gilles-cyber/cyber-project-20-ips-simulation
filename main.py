# IPS Simulation

from core.ips_engine import analyze_and_block

# Load traffic logs
with open("data/traffic_logs.txt", "r") as file:
    logs = file.readlines()

print("=== IPS ACTIVE DEFENSE ===\n")

# Analyze traffic and block threats
for log in logs:
    log = log.strip()

    action = analyze_and_block(log)

    if action:
        print(action)
