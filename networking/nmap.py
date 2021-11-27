import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from concurrent.futures import as_completed
import ipaddress
import re
import socket
import logging
import argparse

# Configuration
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535


def parse_args():
    parser = argparse.ArgumentParser(
        description="""Python nmap and ddos script"""
    )
    parser.add_argument(
        "-l",
        "--level",
        choices=["INFO", "WARNING", "ERROR", "CRITICAL", "DEBUG"],
        required=False,
        dest="debug",
        default="INFO",
        help="""level of logging""",
        type=str,
    )
    parser.add_argument(
        "-t",
        "--target",
        required=True,
        dest="ip_address",
        help="""Address ip that you want to scan""",
        type=str,
    )
    parser.add_argument(
        "-p",
        "--port-range",
        required=True,
        dest="port_range",
        help="""Port range that you want to scan""",
        type=str,
    )

    return parser.parse_args()


def validate_ip_address(ip_address):
    try:
        valid_address = ipaddress.ip_address(ip_address)
        logging.info(f"{valid_address} is a valid address")
    except SystemExit:
        logging.error(f"{ip_address} is not a valid address")


def extract_port_range(port_range):
    port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
    if port_range_valid:
        # We're extracting the low end of the port scanner range the user want to scan.
        port_min = int(port_range_valid.group(1))
        # We're extracting the upper end of the port scanner range the user want to scan.
        port_max = int(port_range_valid.group(2))

        return port_max,port_min


def connection(ip_address,port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ip_address, port))
            return f"# Port {port} opened in {ip_address}"
    except:
        pass


def main():
    start = time.perf_counter()
    args = parse_args()

    logging.basicConfig(
        format="%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s",
        level=args.debug,
    )

    validate_ip_address(args.ip_address)
    extract_port_range(args.port_range)
    max_port, min_port = extract_port_range(args.port_range)
    ports = [ports for ports in range(min_port,max_port +1)]

    # Multiprocessing, if not, that script is too slow
    with ProcessPoolExecutor(max_workers=13) as executor:
        futures = [executor.submit(connection, args.ip_address, port) for port in ports]
        for future in as_completed(futures):
            if future.result() is not None:
                print(future.result())

    finish = time.perf_counter()

    print(f"Finished in {round(finish - start, 2)} second(s)")


if __name__ == '__main__':
    main()