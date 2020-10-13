from tkinter import *
import tkinter as tk
import subprocess


def ping():
    cmd = ["ping", entry_text.get(), "-n", "2"]
    output = subprocess.check_output(cmd)

    print('>', output)
    # put result in label
    result['text'] = output.decode('utf-8')

def button_1():
    # define new text
    new_text = "8.8.8.8"
    # set connected text variable to new_text
    entry_text.set(new_text)

def button_2():
    # define new text 
    new_text = "192.168.35.101"
    # set connected text variable to new_text
    entry_text.set(new_text)

def button_3():
    # define new text 
    new_text = "192.168.35.103"
    # set connected text variable to new_text
    entry_text.set(new_text)

def button_4():
    # define new text 
    new_text = "192.168.35.104"
    # set connected text variable to new_text
    entry_text.set(new_text)

def button_5():
    # define new text 
    new_text = "192.168.35.105"
    # set connected text variable to new_text
    entry_text.set(new_text)

def button_6():
    # define new text 
    new_text = "192.168.35.106"
    # set connected text variable to new_text
    entry_text.set(new_text)

def button_7():
    # define new text 
    new_text = "192.168.35.107"
    # set connected text variable to new_text
    entry_text.set(new_text)

def button_8():
    # define new text 
    new_text = "192.168.35.100"
    # set connected text variable to new_text
    entry_text.set(new_text)

def button_9():
    # define new text 
    new_text = "192.168.35.50"
    # set connected text variable to new_text
    entry_text.set(new_text)

def button_10():
    # define new text 
    new_text = "UNKNOWN"
    # set connected text variable to new_text
    entry_text.set(new_text)

def button_11():
    # define new text 
    new_text = "ALL-Hosts"
    # set connected text variable to new_text
    entry_text.set(new_text)

root = tk.Tk()
entry_text = tk.StringVar()


root.geometry('1000x800')
root.title("Sys Admin Py Ping Tool")

tk.Label(root, text="Enter target IP or host as required.").pack(pady=20)
entry = tk.Entry(root, textvariable=entry_text).pack()
tk.Button(root,text="Ping Test", command=ping).pack(pady=10)

button_1 = tk.Button(root,text="Google",command=button_1, padx=5, pady=3, height =5, width =10)
button_2 = tk.Button(root,text="SW2",command=button_2, padx=5, pady=3, height =5, width =10)
button_3 = tk.Button(root,text="SW3",command=button_3, padx=5, pady=3, height =5, width =10)
button_4 = tk.Button(root,text="SW4",command=button_4, padx=5, pady=3, height =5, width =10)
button_5 = tk.Button(root,text="SW5",command=button_5, padx=5, pady=3, height =5, width =10)
button_6 = tk.Button(root,text="SW6",command=button_6, padx=5, pady=3, height =5, width =10)
button_7 = tk.Button(root,text="SW7",command=button_7, padx=5, pady=3, height =5, width =10)
button_8 = tk.Button(root,text="RT1",command=button_8, padx=5, pady=3, height =5, width =10)
button_9 = tk.Button(root,text="VPC",command=button_9, padx=5, pady=3, height =5, width =10)
button_10 = tk.Button(root,text="Web_server",command=button_10, padx=5, pady=3, height =5, width =10)
button_11 = tk.Button(root,text="ALL",command=button_11, padx=5, pady=3, height =5, width =10)


# label for ping result
result = tk.Label(root)
result.pack()

button_1.pack(side = LEFT)
button_2.pack(side = LEFT)
button_3.pack(side = LEFT)
button_4.pack(side = LEFT)
button_5.pack(side = LEFT)
button_6.pack(side = LEFT)
button_7.pack(side = LEFT)
button_8.pack(side = LEFT)
button_9.pack(side = LEFT)
button_10.pack(side = LEFT)
button_11.pack(side = LEFT)
root.mainloop()