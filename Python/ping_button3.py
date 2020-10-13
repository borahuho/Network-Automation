from tkinter import *
import tkinter as tk
import subprocess


running = False
idle_status = 'Select device and press "Ping test" '

def ping():
    global running
    running = True
    if running:
        cmd = ["ping", entry_text.get(), "-n", "4"]
        try:
            output = subprocess.check_output(cmd,universal_newlines=True, shell=True).splitlines()
            print(output)
            for i in output:
                if "Packets" in i: packet_loss = int(re.search(r'\d+', str(re.findall(r'Lost =\s\d*',i))).group())
                if "Minimum" in i: average_latency = int(re.search(r'\d+', str(re.findall(r'Average =\s\d*',i))).group())
        except:
            Fail = "Host offline"
            print(Fail)
            return False


    Status.configure(text="Result: ", background="Grey")
    StatusPacketLoss.configure(text="Packet(s) lost: {0}".format(packet_loss))
    StatusPacketLoss.configure(background=status_color(packet_loss))
    StatusLatency.configure(text="Average ms: {0}".format(average_latency))
    StatusLatency.configure(background=status_color(average_latency))


def status_color(x):
    # Determine Packet Loss Color
    if x == 0:
        color = "Green"
    elif x <= 4:
        color = "Red"

    # Determine Average Latency Color
    if x <= 35: color = "Green"
    if 35 < x < 70: color= "Yellow"
    if x >= 70: color = "Red"

    return color

"""

#New class button to define buttons
class button:
    def __init__(self,ip):
        self.ip = ip


button_1 = button("8.8.8.8")


def set_text(text):
    entry.delete(0,END)
    entry_text.set(0,text)
    return

"""

button_name_list = [
    'button_1'
]

button_label_list = [
    'Google'
]

button_command_list = [
    'new_text = "8.8.8.8"'
]

def button_1():
    new_text = "8.8.8.8"
    entry_text.set(new_text)

def button_2():
    new_text = "192.168.35.101"
    entry_text.set(new_text)

def button_3(): 
    new_text = "192.168.35.103"
    entry_text.set(new_text)

def button_4():
    new_text = "192.168.35.104"
    entry_text.set(new_text)

def button_5():
    new_text = "192.168.35.105"
    entry_text.set(new_text)

def button_6():
    new_text = "192.168.35.106"
    entry_text.set(new_text)

def button_7():
    new_text = "192.168.35.107"
    entry_text.set(new_text)

def button_8():
    new_text = "192.168.35.100"
    entry_text.set(new_text)

def button_9():
    new_text = "192.168.35.50"
    entry_text.set(new_text)

def button_10():
    new_text = "UNKNOWN"
    entry_text.set(new_text)

def button_11():
    new_text = "ALL-Hosts"
    entry_text.set(new_text)

root = tk.Tk()
entry_text = tk.StringVar()

zip_list = zip(button_name_list, button_label_list, button_command_list)

button_dict = {}
for name, label, cmd in zip_list:
    button = tk.Button(root, text=label, width=15, command=cmd).pack()
    button_dict[name] = button


locals().update(button_dict)
root.update()

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


Status = Label(root, text = idle_status, height="0", width="30", background="Grey")
Status.pack(pady=1)
StatusPacketLoss = Label(root, height="0", width="30", background="Grey")
StatusPacketLoss.pack()
StatusLatency = Label(root, height="0", width="30", background="Grey")
StatusLatency.pack()

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