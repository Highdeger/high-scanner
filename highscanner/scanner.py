import socket
from struct import pack


class PortScanner:
    @staticmethod
    def get_ip_from_hostname(hostname: str):
        """
        Fetch IP of a hostname through DNS.
        :param hostname: string, name to resolve through DNS
        :return: string, result IP
        """
        return str(socket.gethostbyname(hostname))

    # return: bool
    @staticmethod
    def is_port_open(dest_ip: str, port: int, timeout: float):
        """
        Check if a port is open.
        :param dest_ip: string, IP
        :param port: int, port number
        :param timeout: float, timeout in seconds
        :return: bool
        """
        host_ip = dest_ip.replace(' ', '')

        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.settimeout(timeout)

        result = my_socket.connect_ex((host_ip, port))
        my_socket.close()
        if result == 0:
            return True, result
        else:
            return False, result

    # @staticmethod
    # def is_ports_open_syn(host_ip, port, timeout, source_ip):
    #     host_ip = host_ip.replace(' ', '')
    #
    #     # create a raw socket
    #     so = None
    #     try:
    #         so = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    #     except socket.error as msg:
    #         print('Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    #
    #     # tell kernel not to put in headers, since we are providing it, when using IPPROTO_RAW this is not necessary
    #     so.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    #
    #     # ip header fields
    #     ip_ihl = 5
    #     ip_ver = 4
    #     ip_tos = 0
    #     ip_tot_len = 0  # kernel will fill the correct total length
    #     ip_id = 54321  # Id of this packet
    #     ip_frag_off = 0
    #     ip_ttl = 255
    #     ip_proto = socket.IPPROTO_TCP
    #     ip_check = 0  # kernel will fill the correct checksum
    #     ip_saddr = socket.inet_aton(source_ip)  # Spoof the source ip address if you want to
    #     ip_daddr = socket.inet_aton(host_ip)
    #
    #     ip_ihl_ver = (ip_ver << 4) + ip_ihl
    #
    #     # the ! in the pack format string means network order
    #     ip_header = pack('!BBHHHBBH4s4s', ip_ihl_ver, ip_tos, ip_tot_len, ip_id, ip_frag_off, ip_ttl, ip_proto,
    #                      ip_check, ip_saddr, ip_daddr)
    #
    #     # tcp header fields
    #     tcp_source = 1234  # source port
    #     tcp_dest = 80  # destination port
    #     tcp_seq = 454
    #     tcp_ack_seq = 0
    #     tcp_doff = 5  # 4 bit field, size of tcp header, 5 * 4 = 20 bytes
    #     # tcp flags
    #     tcp_fin = 0
    #     tcp_syn = 1
    #     tcp_rst = 0
    #     tcp_psh = 0
    #     tcp_ack = 0
    #     tcp_urg = 0
    #     tcp_window = socket.htons(5840)  # maximum allowed window size
    #     tcp_check = 0
    #     tcp_urg_ptr = 0
    #
    #     tcp_offset_res = (tcp_doff << 4) + 0
    #     tcp_flags = tcp_fin + (tcp_syn << 1) + (tcp_rst << 2) + (tcp_psh << 3) + (tcp_ack << 4) + (tcp_urg << 5)
    #
    #     # the ! in the pack format string means network order
    #     tcp_header = pack('!HHLLBBHHH', tcp_source, tcp_dest, tcp_seq, tcp_ack_seq, tcp_offset_res, tcp_flags,
    #                       tcp_window, tcp_check, tcp_urg_ptr)
    #
    #     user_data = b'Deo Vitali'
    #
    #     # pseudo header fields
    #     placeholder = 0
    #     protocol = socket.IPPROTO_TCP
    #     tcp_length = len(tcp_header) + len(user_data)
    #
    #     push = pack('!4s4sBBH', ip_saddr, ip_daddr, placeholder, protocol, tcp_length)
    #     push = push + tcp_header + user_data
    #
    #     tcp_check = PortScanner.msg_checksum(push)
    #     # print tcp_checksum
    #
    #     # make the tcp header again and fill the correct checksum - remember checksum is NOT in network byte order
    #     tcp_header = pack('!HHLLBBH', tcp_source, tcp_dest, tcp_seq, tcp_ack_seq, tcp_offset_res, tcp_flags,
    #                       tcp_window) + pack('H', tcp_check) + pack('!H', tcp_urg_ptr)
    #
    #     # final full packet - syn packets dont have any data
    #     packet = ip_header + tcp_header + user_data
    #
    #     # Send the packet finally - the port specified has no effect
    #     a = so.sendto(packet, (host_ip, port))  # put this in a loop if you want to flood the target
    #     print('a', a)
    #
    #     # my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW)
    #     # my_socket.settimeout(timeout)
    #     # result = my_socket.connect_ex((host_ip, port))
    #     # my_socket.close()
    #     # if result == 0:
    #     #     return True
    #     # else:
    #     #     return False
    #
    # # checksum functions needed for calculation checksum
    # @staticmethod
    # def msg_checksum(msg):
    #     sum_result = 0
    #     # i in every second index
    #     msg_str = str(msg)
    #     for i in range(0, len(msg_str), 2):
    #         # push 8 zeros from right for second char
    #         weight = ord(msg_str[i]) + (ord(msg_str[i + 1]) << 8)
    #         sum_result = sum_result + weight
    #     sum_result = (sum_result >> 16) + (sum_result & 0xffff)
    #     sum_result = sum_result + (sum_result >> 16)
    #     # invert bits and put in 4-byte frame
    #     sum_result = ~sum_result & 0xffff
    #     return sum_result
