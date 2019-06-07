from tkinter import *
import requests
from threading import Thread
import time


class TallyThead(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            api_url = 'http://127.0.0.1:5000'
            url = api_url + '/tally/value'
            tally = requests.get(url)

            rjson = tally.json()

            global tally_value

            tally_value = rjson['tally_value']

            print(tally_value)
            time.sleep(1)


class Gui:

    def __init__(self):
        pass

    def open_gui(self):
        root = Tk()

        root.title("Pad sprint 5")
        root.geometry("400x400+300+300")

        tally = tally_value
        print(tally, " Some random shit")

        if tally == 1:
            tally1 = Label(root, text="Tally 1 ON")
            tally2 = Label(root, text="Tally 2")
            tally3 = Label(root, text="Tally 3")
            tally4 = Label(root, text="Tally 4")

            tally1.grid(row=0)
            tally2.grid(row=1)
            tally3.grid(row=0, column=1)
            tally4.grid(row=1, column=1)

        if tally == 2:
            tally1 = Label(root, text="Tally 1")
            tally2 = Label(root, text="Tally 2 ON")
            tally3 = Label(root, text="Tally 3")
            tally4 = Label(root, text="Tally 4")

            tally1.grid(row=0)
            tally2.grid(row=1)
            tally3.grid(row=0, column=1)
            tally4.grid(row=1, column=1)

        root.mainloop()


tally_thread = TallyThead()
tally_thread.start()
print('taart')
gui = Gui()
gui.open_gui()
