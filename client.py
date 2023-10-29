import socket
import sys
from faker import Faker

fake = Faker("jp-JP")
name = fake.name()

#create TCP/IP socket
sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)

server_address = "socket_file"
print("connecting to {}".format(server_address))

try:
    sock.connect(server_address)

except socket.error as err:
    print(err)
    sys.exit(1)

try:
    message = input("Please input message -- > ")
    message = message + ": by " + name
    sock.sendall(message)

    sock.settimeout(2)

    try:
        while True:
            data = str(sock.recv(32))

            if data:
                print("Server response: " + data)
            else:
                break
    
    except(TimeoutError):
        print("Socket timeout, ending listening for server message")

finally:
    print("closing socket")
    sock.close()
