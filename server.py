import socket
import os 
from faker import Faker

def main():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    server_address = "/tmp/server_file"
    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    print("starting up on {}".format(server_address))

    sock.bind(server_address)

    while True:
        print("\nwaiting to recieve message")

        data, address = sock.recvfrom(4096)
        print("receive {} bytes data from {}".format(len(data), address))

        if data:
            fake = Faker()
            fake_company = fake.company().encode()
            sent = sock.sendto(fake_company, address)
            print("sent {} data back to {}".format(sent, address))

if __name__ == "__main__":
    main()
