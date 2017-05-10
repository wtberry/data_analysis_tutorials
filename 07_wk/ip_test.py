import ipaddress as ip

fn = open('networks.txt', 'r').readlines()
fn = [ip.ip_network(item.strip()) for item in fn]

fa = open('addrs.txt', 'r').readlines()
fa = [ip.ip_address(item.strip()) for item in fa]

for n in fn:
    for a in fa:
        if a in n:
            print(a, 'is in', n)