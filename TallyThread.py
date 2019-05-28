import socket
from socket import error as socket_error
import threading
import requests

TCP_IP = '127.0.0.1'
TCP_PORT = 8099
MSG_SIZE = 1024
api_url = 'http://127.0.0.1:5000'

# Maakt TCP/IP socket aan
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((TCP_IP, TCP_PORT))


def get_data(socket):
    while True:
        try:
            data = socket.recv(MSG_SIZE)
            data = str(data)
            antwoord = data.split(' ')
            tallyIndex(antwoord[2])

            if not data:
                break
        except socket_error as e:
            print(e)
            break


# Maakt thread aan voor socket connectie
iThread = threading.Thread(target=get_data, args=(socket,))
iThread.start()
print("Connected...")


def tallyIndex(response):
    try:
        # checkt hoeveel tally lights zijn aangesloten en stuurt dit door naar interface
        tallyAAN = api_url + '/tallyAAN={}'.format(response)
        switch = requests.get(tallyAAN)
        for i in range(len(response)):
            if response.index("1") == i:
                url = api_url + '/tally={}'.format(i)
                tally = requests.get(url)
                print(i, " taart")

    except Exception as e:
        print(e)
    finally:
        print(response)
        return response


socket.send(bytes("SUBSCRIBE TALLY\r\n"))