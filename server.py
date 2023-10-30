import socket
import os
from faker import Faker

def main():
    fake = Faker("jp-JP")
    name = fake.name()
    print(name)


    sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)

    server_address = "socket_file"


    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    print("Starting up on {}".format(server_address))

    sock.bind(server_address)

    # connect
    sock.listen(1)

    while True:
        connection, client_address = sock.accept()

        try:
            print("connection from ",client_address)

            while True:
                data = connection.recv(1024)
                data_str = data.decode("utf-8")
                print("Received " + data_str)

                if data:
                    message = input("Please input message --> ")
                    response = "From " + name + ": " + message

                    connection.sendall(response.encode())
                
                else:
                    print("no data from",client_address)
                    break
        
        finally:
            print("CLosing current connection")
            connection.close()

if __name__ == "__main__":
    main()