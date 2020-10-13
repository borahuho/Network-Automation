from tkinter import *
import os

def Check(self):
    
    hosts = ['8.8.8.8', '192.168.178.212', '192.168.178.213', '192.168.178.214']
    buttons = [self.button1, self.button2, self.button3, self.button4]
    
    for x, i in enumerate(hosts):

        response = os.system("ping -n 1 -w 500 " + i + " > nul")

        if response == 0:
            buttons[x].background_color = green
        else:
            buttons[x].background_color = red

    pass

