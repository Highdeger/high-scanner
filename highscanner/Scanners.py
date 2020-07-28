import socket
import re
from datetime import datetime


class PortScanner:
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

    @staticmethod
    def is_ipv4(ip: str):
        regex_ipv4 = r''
        regex_ipv4 += r'^((25[1-5])|(2[1-4][1-9])|(1[1-9][1-9])|000|00|0|[1-9]|[1-9][1-9]|(0[1-9])|(00[1-9])|(0[1-9][1-'
        regex_ipv4 += r'9]))\.((25[1-5])|(2[1-4][1-9])|(1[1-9][1-9])|000|00|0|[1-9]|[1-9][1-9]|(0[1-9])|(00[1-9])|(0[1-'
        regex_ipv4 += r'9][1-9]))\.((25[1-5])|(2[1-4][1-9])|(1[1-9][1-9])|000|00|0|[1-9]|[1-9][1-9]|(0[1-9])|(00[1-9])|'
        regex_ipv4 += r'(0[1-9][1-9]))\.((25[1-5])|(2[1-4][1-9])|(1[1-9][1-9])|000|00|0|[1-9]|[1-9][1-9]|(0[1-9])|(00[1'
        regex_ipv4 += r'-9])|(0[1-9][1-9]))$'

        return re.match(regex_ipv4, ip)
