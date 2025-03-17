import re
from ping3 import ping
from functools import partial
from concurrent.futures import ThreadPoolExecutor



def extract_servers(file):
    title_p = '[A-Z]{2,}\s?\w*\s-\s(.*)$'
    ip_p = '\w{2}-\w*-\d\s*-\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

    servers = {}
    current_title = 'Unknown'

    with open(file) as file:
        for line in file.readlines():
            line = line.strip()

            if title:=re.fullmatch(title_p, line):
                current_title = title.groups()[0]

            elif server:=re.fullmatch(ip_p, line):

                if not servers.get(current_title):
                    servers[current_title] = []

                servers[current_title].append(server.groups()[0])

        return servers


def retry(count=2, on_fail=None):
    def inner(function):
        def impl(*args, **kwargs):
            for _ in range(count):
                response = function(*args, **kwargs)
                if response:
                    return response
            return on_fail
        return impl
    return inner


@retry(1)
def try_ping(address):
    return ping(address)


def _ping_server(target, count):
    ping_data = []

    for _ in range(count):
        ping_time = try_ping(target)

        if not ping_time:
            return -1

        ping_data.append(
                ping_time*1000
            )

    return sum(ping_data)/count


def ping_servers(servers, ping_count=3):

    ping_report = {server:[] for server in servers.keys()}
    ping_method = partial(_ping_server, count=ping_count)

    for server, ips in servers.items():
        print(server)
        pool = ThreadPoolExecutor(max_workers=len(ips))
        data = pool.map(ping_method, ips)
        ping_report[server] = [datum for datum in data]

    return ping_report


def clean_ping_report(ping_data):
    for zone, ping_values in ping_data.items():
        ping_values = [value for value in ping_values if value > 0]
        value = round(sum(ping_values)/len(ping_values))
        ping_data[zone] = value

    return ping_data


def print_ping_report(ping_data):
    for server, ping_value in sorted(ping_data.items(), key=lambda x:x[1]):
        print(f"{ping_value}\t{server}")

servers = extract_servers('/home/prajwal/gitlib/pys/servers_ping.txt')
response_time_data = ping_servers(servers, ping_count=1)
cleaned_data = clean_ping_report(response_time_data)
print_ping_report(cleaned_data)
