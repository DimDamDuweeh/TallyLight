import socket
import threading

TCP_IP = '127.0.0.1'
TCP_PORT = 8099
MSG_SIZE = 1024

# Maakt TCP/IP socket aan
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((TCP_IP, TCP_PORT))


def get_data(socket):
    while True:
        try:
            data = socket.recv(MSG_SIZE)
            data = str(data, 'utf-8')
            antwoord = data.split(' ')
            tallyIndex(antwoord[2])

            if not data:
                break
        except socket.error as e:
            print(e)
            break


# Maakt thread aan voor socket connectie
iThread = threading.Thread(target=get_data, args=(socket,))
iThread.start()
print("Connected...")


def tallyIndex(response):
    try:
        if response.index("1") == 0:
            print("Camera 1")
        elif response.index("1") == 1:
            print("Camera 2")
        elif response.index("1") == 2:
            print("Camera 3")

    except Exception as e:
        print(e)
    finally:
        print(response)
        return response


socket.send(bytes("SUBSCRIBE TALLY\r\n", 'utf-8'))
