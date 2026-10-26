"""
Project: port-scanner

File: scanner.py

Description: 

Created by: Gavin Main

Date Finalized: 
"""

import socket

"""
Attempts to establish a TCP connection to a spcified port.

Args:
    target (str): IP address of the target host.
    port (int): TCP port number to scan.
    timeout (float): Connection timeout in seconds.

Returns:
    bool: True if the port is open, False otherwise.
"""
def scan_port(target, port, timeout=0.5):

    try:
        # Create a TCP socket using IPv4
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            # Set the connection timeout
            sock.settimeout(timeout)

            # Attempt to connect to the target port
            result = sock.connect_ex((target, port))

            # 0 indicates an open port
            return result == 0

    except OSError:
        return False

"""
Scans a range of TCP ports on a target host.

Args:
    target (str): IP address of the target host.
    start_port (int): First port to scan.
    end_port (int): Last port to scan.
    timeout (float): Connection timeout in seconds.

Returns:
    list: A list of open TCP port numbers.
"""
def scan_ports(target, start_port, end_port, timeout=0.5):
    open_ports = []

    # Iterate through the specified port range
    for port in range(start_port, end_port + 1):

        # Check whether the current port is open
        if scan_port(target, port, timeout):
            open_ports.append(port)

    return open_ports

