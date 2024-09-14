import random
import ipaddress

def generate_random_ipv6():
    ip = []
    for _ in range(8):
        segment = hex(random.randint(0, 65535))[2:]  
        ip.append(segment.zfill(4)) 
    return ':'.join(ip)

def validate_ipv6(ip):
    try:
        ipaddress.IPv6Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

def generate_random_dns_code():
    while True:
        ipv6 = generate_random_ipv6()
        if validate_ipv6(ipv6):
            return ipv6

def main():
    try:
        num_codes = int(input("How many codes should I make? "))
        print(f"{num_codes}")
        for _ in range(num_codes):
            print(generate_random_dns_code())
    except ValueError:
        print("Please enter an integer: ")

if __name__ == "__main__":
    main()
