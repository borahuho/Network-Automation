from tkinter import *
from tkinter import ttk

root = Tk()
Label(root, text="Hello, Sys Admin").pack()

button = ttk.Button(root, text = "Submit")
button.pack()


def callback():
    print("Clicked")
button.config(command = callback)

root.mainloop()