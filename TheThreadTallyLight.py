import socket
import threading
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 8099
MSG_SIZE = 1024

# Maakt TCP/IP socket aan
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((TCP_IP, TCP_PORT))


def sendMsg(socket):
    try:
        while True:
            socket.send(bytes("TALLY\r\n", 'utf-8'))
            time.sleep(2)

    except Exception as e:
        print(e)
    finally:
        socket.close()

# Maakt thread aan voor socket connectie
iThread = threading.Thread(target=sendMsg, args=(socket,))
iThread.start()
print("Connected...")



def get_data():
    while True:
        try:
            data = socket.recv(MSG_SIZE)
            data = data[9:]
            print(str(data, 'utf-8'))
            if not data:
                break

        except socket.error:
            print("error occured.")
            break

    while True:
        get_data()
        break

def tallyswitcher():
    for x in range(len(get_data().data)):
        print("hallo")


