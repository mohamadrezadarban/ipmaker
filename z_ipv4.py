import random
import ipaddress

def generate_random_ip(ip_range_start, ip_range_end):
    while True:
        ip = []
        for i in range(4):
            ip.append(str(random.randint(ip_range_start[i], ip_range_end[i])))
        ip_str = '.'.join(ip)
        
        try:
            ipaddress.IPv4Address(ip_str)
            return ip_str
        except ipaddress.AddressValueError:
            continue

def generate_random_dns_code(ip_range_start, ip_range_end):
    return generate_random_ip(ip_range_start, ip_range_end)

def main():
    try:
        num_codes = int(input("How many codes should I make?"))
        print(f"{num_codes}:")
        
        ip_range_start = [37, 236, 0, 0]
        ip_range_end = [37, 236, 255, 255]
        
        for _ in range(num_codes):
            print(generate_random_dns_code(ip_range_start, ip_range_end))
    except ValueError:
        print("Please enter an integer: ")

if __name__ == "__main__":
    main()
