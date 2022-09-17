"""
Módulo udp_server_t.py:
    Módulo que mediante el sockets crea un servidor del tipo UDP, y permite
    enviar y recibir datos del cliente.
"""
__author__ = "Paula Jesica Vergara De Castro"
__maintrainer__ = "Juan Barreto"
__email__ = "paulajve@gmail.com"
__copyright__ = "Copyright 2022"
__version__ = "1.1"

import socket
import sys

# Creación del socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind del socket al puerto
server_address = ("localhost", 10000)
print("Iniciado en {} puerto {}".format(*server_address))
sock.bind(server_address)

while True:
    print("\nesperando recibir mensaje")
    data, address = sock.recvfrom(4096)

    print("{} bytes recibidos de {}".format(len(data), address))
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print("{} bytes enviados de regreso a {}".format(sent, address))
