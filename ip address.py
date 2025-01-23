def find(ip):
    segments = ip.split('.')
    if len(segments) != 4:
        return False
    for segment in segments:
        if not segment.isdigit() or not (0 <= int(segment) <= 255):
            return False
    return True
ipaddress = "192.163.72.102"
if find(ipaddress):
    print(ipaddress, "is a valid IPv4 address.")
else:
    print(ipaddress, "is not a valid IPv4 address.")
