import socket
import sys
from faker import Faker

def main():
    fake = Faker("jp-JP")
    name = fake.name()
    print(name)


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
        try:
            while True:
                message = input("Please input message -- > ")
                message = "From " + name + ": " + message
                sock.sendall(message.encode("utf-8"))

                sock.settimeout(20)

                data = sock.recv(1024)
                data = data.decode("utf-8")

                if data:
                    print("Server response " + data)
                else:
                    break
        
        except(TimeoutError):
            print("Socket timeout, ending listening for server message")

    finally:
        print("closing socket")
        sock.close()
        
if __name__ == "__main__":
    main()
