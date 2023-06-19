import socket

def get_host_info():
    # Get the hostname of the current machine
    hostname = socket.gethostname()

    # Get the IP addresses and hostnames of all network interfaces
    ip_addresses = []
    hostnames = []

    # Iterate over all network interfaces
    for interface in socket.if_nameindex():
        interface_name = interface[1]
        try:
            # Get the IP address of the interface
            ip = socket.gethostbyname(interface_name)
            ip_addresses.append(ip)

            # Get the hostname of the IP address
            hostname = socket.gethostbyaddr(ip)[0]
            hostnames.append(hostname)
        except socket.error:
            # Skip interfaces that cannot be resolved
            continue

    return ip_addresses, hostnames

# Call the function to get the IP addresses and hostnames
ip_addresses, hostnames = get_host_info()

# Display the IP addresses and hostnames
for ip, hostname in zip(ip_addresses, hostnames):
    print(f"IP Address: {ip}\tHostname: {hostname}")
