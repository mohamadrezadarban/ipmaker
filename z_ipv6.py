import random
import ipaddress

def generate_random_ipv6():
    # Generate a random IPv6 address
    ip = []
    for _ in range(8):
        segment = hex(random.randint(0, 65535))[2:]  # Generate a random 16-bit segment
        ip.append(segment.zfill(4))  # Ensure the segment is 4 characters long
    return ':'.join(ip)

def validate_ipv6(ip):
    try:
        ipaddress.IPv6Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

def generate_random_dns_code():
    # Random DNS Code pattern (example: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx)
    while True:
        ipv6 = generate_random_ipv6()
        if validate_ipv6(ipv6):
            return ipv6

def main():
    try:
        num_codes = int(input("چندتا کد بسازم؟ "))
        print(f"{num_codes} کد دی‌ان‌اس رندوم:")
        for _ in range(num_codes):
            print(generate_random_dns_code())
    except ValueError:
        print("لطفاً یک عدد صحیح وارد کنید.")

if __name__ == "__main__":
    main()