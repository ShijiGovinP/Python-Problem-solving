def is_valid_ipv4(ip):
    segments = ip.split('.')
    if len(segments) != 4:
        return False
    for segment in segments:
        if not segment.isdigit() or not (0 <= int(segment) <= 255):
            return False
    return True
ip_address = "192.163.72.102"
if is_valid_ipv4(ip_address):
    print(f"{ip_address} is a valid IPv4 address.")
else:
    print(f"{ip_address} is not a valid IPv4 address.")
