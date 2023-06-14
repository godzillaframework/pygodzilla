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