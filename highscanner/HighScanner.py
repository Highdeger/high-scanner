import socket
import sys
from datetime import datetime


class HighScanner:
    @staticmethod
    def get_ip_from_hostname(hostname: str):
        try:
            return str(socket.gethostbyname(hostname))
        except socket.gaierror:
            raise Exception('Cannot resolve the hostname through dns.')

    @staticmethod
    def is_port_open(host_ip: str, port: int, timeout=0.05):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.settimeout(0.05)
        result = my_socket.connect_ex((host_ip, port))
        my_socket.close()
        if result == 0:
            return True
        else:
            return False
