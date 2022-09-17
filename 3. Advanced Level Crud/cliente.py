# A command line client for the date server.

import sys
import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("localhost", 10000)
message = b"Este es el mensaje. A ser repetido."

try:

    # Send data
    print("enviando {!r}".format(message))
    sent = sock.sendto(message, server_address)

    # Receive response
    print("esperando recibir")
    data, server = sock.recvfrom(4096)
    print("recibido {!r}".format(data))

finally:
    print("socket cerrado")
    sock.close()
