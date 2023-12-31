import logging
import signal
import socket
import sys
import time
import uuid
from typing import Callable

def get_next_available_port(port: int) -> int:
    def is_port_available() -> bool:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind(("localhost", port))
            return True
        except socket.error:
            return False
        finally:
            sock.close()

    while not is_port_available():
        port += 1

    return port


def unique_id() -> str:
    return str(uuid.uuid4()).replace("-", "")


def current_time_us() -> int:
    return int(time.time() * 1e6)


def register_signal_term(sigterm_handler: Callable):
    original_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)

    signal.signal(signal.SIGTERM, sigterm_handler)
    signal.signal(signal.SIGINT, original_sigint_handler)

    if sys.platform == "win32":
        signal.signal(signal.SIGBREAK, sigterm_handler)
    else:
        signal.signal(signal.SIGQUIT, sigterm_handler)
        signal.signal(signal.SIGHUP, sigterm_handler)


def log_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exc:  
            logging.exception(exc)
            return None

    return wrapper