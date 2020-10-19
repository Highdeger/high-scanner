import sys
from getopt import getopt, GetoptError
import socket
from highscanner import PortScanner, Utility
from time import time
import urllib.request as req


version = '0.0.1'
verbose = False
is_output = False
first_time = 0
source_ip = ''


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_help():
    title = 'High Scanner v{} by Highdeger'.format(version)
    print(title)
    print('-' * len(title))
    print('USAGE: (sudo) highscanner ADDRESS PORT TIMEOUT'
          '\nUSAGE: (sudo) highscanner -a ADDRESS -p PORT [-t TIMEOUT -v]'
          '\nEXAMPLE: $ sudo highscanner 204.24-93.14-2.81 22,78-82 0.12'
          '\nEXAMPLE: $ sudo highscanner -a 204.24-93.14-2.81 -p 22,78-82 -t 0.12'
          '\nParameters:'
          '\n-h, --help\t\t\tprint this help'
          '\n-a [ADDRESS], --address [ADDRESS]\t\t\thostname or ip or ip-range'
          '\n-p [PORT], --port [PORT]\t\t\tport or port-range'
          '\n-t [SEC], --timeout [SEC]\t\t\ttimeout by seconds (default=0.1s)'
          '\n-v, --verbose\t\t\tshow all results in IP-Range mode (One-IP mode have verbose activated)')
    sys.exit(0)


def main(argv):
    global first_time
    first_time = time()
    global source_ip
    if source_ip == '':
        source_ip = req.urlopen('https://ident.me').read().decode('utf8')
    elif source_ip == '':
        source_ip = req.urlopen('https://api.ipify.org/').read().decode('utf8')
    global verbose
    global is_output
    address = ''
    port = ''
    timeout = '0.4'
    address_list = list()
    port_list = list()
    syn = False

    if Utility.is_ipv4_pattern(argv[0]) and Utility.is_port_pattern(argv[1]) and 2 <= len(argv) <= 3:
        address_list = Utility.create_ipv4_list(argv[0])
        port_list = Utility.create_port_list(argv[1])
        if len(argv) == 3:
            timeout = argv[2]
    else:
        try:
            opts, misc = getopt(argv, 'hvosa:p:t:i:', ['help', 'verbose', 'output', 'syn', 'address', 'port',
                                                       'timeout'])
        except GetoptError:
            get_help()
            opts = []

        for opt, arg in opts:
            if opt in ['-h', '--help']:
                get_help()
            elif opt in ['-a', '--address']:
                address = arg
            elif opt in ['-p', '--port']:
                port = arg
            elif opt in ['-t', '--timeout']:
                timeout = arg
            elif opt in ['-v', '--verbose']:
                verbose = True
            elif opt in ['-o', '--output']:
                is_output = True
            elif opt in ['-s', '--syn']:
                syn = True

        if Utility.is_ipv4_pattern(address)[0]:
            address_list = Utility.create_ipv4_list(address)

        if Utility.is_port_pattern(port)[0]:
            port_list = Utility.create_port_list(port)

    if len(address_list) != 0 and len(port_list) != 0:
        scan_list(address_list, port_list, float(timeout), '{0} : {1}'.format(address, port), is_output)
    else:
        print('Err-600: IP or port is missing or wrong formatted.')
        sys.exit(600)


# ip_list: list(str), port_list: list(int), timeout: float
def scan_list(ip_list, port_list, timeout, ip_port_pattern, output):
    for x1 in range(len(ip_list)):
        for x2 in range(len(port_list)):
            try:
                print('Scanning... {0:<15s}:{1:<5d}'.format(ip_list[x1], port_list[x2]), end='')
                print(end='\r')
                if PortScanner.is_port_open(ip_list[x1], port_list[x2], timeout)[0]:
                    if not output:
                        print('IP: {0:<15s} Port: {1:<5d} {2}is open{3}'.format(ip_list[x1], port_list[x2],
                                                                                Colors.OKGREEN, Colors.ENDC))
                    else:
                        if verbose:
                            print('{0:<15s}:{1:<5d}:open'.format(ip_list[x1], port_list[x2]) + ' ' * 7)
                        else:
                            print('{0:<15s}:{1:<5d}'.format(ip_list[x1], port_list[x2]) + ' ' * 11)
                else:
                    if (len(ip_list) == 1 and len(port_list) == 1) or \
                            ((len(ip_list) > 1 or len(port_list) > 1) and verbose):
                        if not output:
                            print('IP: {0:<15s} Port: {1:<5d} {2}gets timeout{3}'.format(ip_list[x1], port_list[x2],
                                                                                         Colors.FAIL, Colors.ENDC))
                        else:
                            print('{0:<15s}:{1:<5d}:timeout'.format(ip_list[x1], port_list[x2]) + ' ' * 4)

            except socket.herror:
                print('Err-601: Cannot connect to server. (IP:Port -> {0:<15s}:{1:<5d})'.format(ip_list[x1],
                                                                                                port_list[x2]))
            except socket.gaierror:
                print('Err-602: Cannot resolve the hostname through dns. (IP:Port -> {0:<15s}:{1:<5d})'
                      .format(ip_list[x1],
                              port_list[x2]))
            except socket.error:
                print('Err-603: Socket error. (IP:Port -> {0:<15s}:{1:<5d})'.format(ip_list[x1],
                                                                                    port_list[x2]))
            except KeyboardInterrupt:
                print('Err-604: Terminated by user. (IP:Port -> {0:<15s}:{1:<5d})'.format(ip_list[x1],
                                                                                          port_list[x2]))
                sys.exit(604)
    # print('Scan finished.                   ')
    task_time = time() - first_time
    print('Scan finished. ({0}) ({1:.2f}s)'.format(ip_port_pattern, task_time))
    print('source_ip', source_ip)


if __name__ == '__main__':
    main(sys.argv[1:])
    sys.exit(0)
