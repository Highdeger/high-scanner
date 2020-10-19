import re


class Utility:

    # ip: str
    # return: bool
    @staticmethod
    def is_ipv4_classic_15chars(ip):
        # regex ipv4 classic multiline
        re_ipv4 = r''
        re_ipv4 += r'^((25[1-5])|(2[1-4][1-9])|(1[1-9][1-9])|000|00|0|[1-9]|[1-9][1-9]|(0[1-9])|(00[1-9])|(0[1-9][1-9])'
        re_ipv4 += r'|( [1-9])|( [1-9] )|([1-9] )|(  [1-9])|([1-9]  )|( [1-9][1-9])|([1-9][1-9] ))\.((25[1-5])|(2[1-4]['
        re_ipv4 += r'1-9])|(1[1-9][1-9])|000|00|0|[1-9]|[1-9][1-9]|(0[1-9])|(00[1-9])|(0[1-9][1-9])|( [1-9])|( [1-9] )|'
        re_ipv4 += r'([1-9] )|(  [1-9])|([1-9]  )|( [1-9][1-9])|([1-9][1-9] ))\.((25[1-5])|(2[1-4][1-9])|(1[1-9][1-9])|'
        re_ipv4 += r'000|00|0|[1-9]|[1-9][1-9]|(0[1-9])|(00[1-9])|(0[1-9][1-9])|( [1-9])|( [1-9] )|([1-9] )|(  [1-9])|('
        re_ipv4 += r'[1-9]  )|( [1-9][1-9])|([1-9][1-9] ))\.((25[1-5])|(2[1-4][1-9])|(1[1-9][1-9])|000|00|0|[1-9]|[1-9]'
        re_ipv4 += r'[1-9]|(0[1-9])|(00[1-9])|(0[1-9][1-9])|( [1-9])|( [1-9] )|([1-9] )|(  [1-9])|([1-9]  )|( [1-9][1-9'
        re_ipv4 += r'])|([1-9][1-9] ))$'
        return re.match(re_ipv4, ip)

    # ip: str
    # return: bool, str
    @staticmethod
    def is_ipv4_pattern(ip):
        if ip.count('.') == 3:
            ips = ip.split('.')
            for x in range(len(ips)):
                if ips[x].count(',') != 0:
                    ips_n = ips[x].split(',')
                    for y in range(len(ips_n)):
                        if ips_n[y].count('-') == 1:
                            range_ab = ips_n[y].split('-')
                            if range_ab[0] > range_ab[1]:
                                range_ab[0], range_ab[1] = range_ab[1], range_ab[0]
                            try:
                                for z in range(int(range_ab[0]), int(range_ab[1]) + 1):
                                    if 0 > z or z > 255:
                                        return False, 'range number lesser than 0 or greater than 255'
                            except ValueError:
                                return False, 'non-number range part'
                        elif ips_n[y].count('-') == 0:
                            try:
                                if 0 > int(ips_n[y]) or int(ips_n[y]) > 255:
                                    return False, 'solo number lesser than 0 or greater than 255'
                            except ValueError:
                                return False, 'non-number solo part'
                        else:
                            return False, 'wrong format'
                else:
                    if ips[x].count('-') == 1:
                        range_ab = ips[x].split('-')
                        if range_ab[0] > range_ab[1]:
                            range_ab[0], range_ab[1] = range_ab[1], range_ab[0]
                        try:
                            for z in range(int(range_ab[0]), int(range_ab[1]) + 1):
                                if 0 > z or z > 255:
                                    return False, 'range number lesser than 0 or greater than 255'
                        except ValueError:
                            return False, 'non-number range part'
                    elif ips[x].count('-') == 0:
                        try:
                            if 0 > int(ips[x]) or int(ips[x]) > 255:
                                return False, 'solo number lesser than 0 or greater than 255'
                        except ValueError:
                            return False, 'non-number solo part'
                    else:
                        return False, 'wrong format'
        else:
            return False, 'not having exactly three dots'
        return True, ''

    # port: str
    # return: bool, str
    @staticmethod
    def is_port_pattern(port):
        if port.count(',') > 0:
            ports = port.split(',')
            for x in range(len(ports)):
                if ports[x].count('-') == 1:
                    ports_n = ports[x].split('-')
                    if ports_n[0] > ports_n[1]:
                        ports_n[0], ports_n[1] = ports_n[1], ports_n[0]
                    try:
                        for z in range(int(ports_n[0]), int(ports_n[1]) + 1):
                            if 0 > z or z > 65535:
                                return False, 'range number lesser than 0 or greater than 65535'
                    except ValueError:
                        return False, 'non-number range part'
                elif ports[x].count('-') == 0:
                    try:
                        if 0 > int(ports[x]) or int(ports[x]) > 65535:
                            return False, 'solo number lesser than 0 or greater than 65535'
                    except ValueError:
                        return False, 'non-number solo part'
                else:
                    return False, 'wrong format'
        else:
            if port.count('-') == 1:
                ports_n = port.split('-')
                if ports_n[0] > ports_n[1]:
                    ports_n[0], ports_n[1] = ports_n[1], ports_n[0]
                try:
                    for z in range(int(ports_n[0]), int(ports_n[1]) + 1):
                        if 0 > z or z > 65535:
                            return False, 'range number lesser than 0 or greater than 65535'
                except ValueError:
                    return False, 'non-number range part'
            elif port.count('-') == 0:
                try:
                    if 0 > int(port) or int(port) > 65535:
                        return False, 'solo number lesser than 0 or greater than 65535'
                except ValueError:
                    return False, 'non-number solo part'
            else:
                return False, 'wrong format'
        return True, ''

    # num: str
    # return: list(int)
    @staticmethod
    def parse_number_pattern_to_list(num):
        numlist = []
        if num != '':
            if num.count(',') > 0:
                n1 = num.split(',')
                for x in range(len(n1)):
                    if n1[x].count('-') == 1:
                        n2 = n1[x].split('-')
                        if n2[0] > n2[1]:
                            n2[0], n2[1] = n2[1], n2[0]
                        for y in range(n2[0], n2[1] + 1):
                            numlist.append(y)
                    elif n1[x].count('-') == 0:
                        numlist.append(int(n1[x]))
            else:
                if num.count('-') == 1:
                    n0 = num.split('-')
                    if n0[0] > n0[1]:
                        n0[0], n0[1] = n0[1], n0[0]
                    for y in range(int(n0[0]), int(n0[1]) + 1):
                        numlist.append(y)
                elif num.count('-') == 0:
                    numlist.append(int(num))
        return numlist

    # ipv4_pattern: str
    # return: list(ipv4_15chars: str)
    @staticmethod
    def create_ipv4_list(ipv4_pattern):
        ipv4_list = []
        t = ipv4_pattern.split('.')
        r = [[], [], [], []]
        for x in range(4):
            r[x] = Utility.parse_number_pattern_to_list(t[x])
        for a in r[0]:
            for b in r[1]:
                for c in r[2]:
                    for d in r[3]:
                        ipv4_list.append('{0:<3d}.{1:<3d}.{2:<3d}.{3:<3d}'.format(a, b, c, d))
        return ipv4_list

    # port_pattern: str
    # return: list(int)
    @staticmethod
    def create_port_list(port_pattern):
        return Utility.parse_number_pattern_to_list(port_pattern)
