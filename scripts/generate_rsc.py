import requests

url = "https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt"
response = requests.get(url)

ips = [line.strip() for line in response.text.splitlines() if line and not line.startswith("#")]

with open("blacklist_combined_full.rsc", "w") as f:
    f.write("/ip firewall address-list\n")
    for ip in ips:
        f.write(f"add address={ip} list=blacklist\n")
