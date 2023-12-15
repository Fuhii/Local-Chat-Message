import os
import socket
import sys

def main():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

    server_address = "/tmp/server_file"
    cilent_address = "/tmp/client_file"

    try:
        os.unlink(cilent_address)
    except FileNotFoundError:
        pass

    sock.bind(cilent_address)

    try:
       message = input("please enter message :").encode()

       print("sending {!r}".format(message))

       send  = sock.sendto(message, server_address)

       print("waiting receive")

       data, server = sock.recvfrom(4096)

       print("receive {!r}".format(data))

    finally:
        print("closing socket")
        sock.close()

if __name__ == "__main__":
    main()



