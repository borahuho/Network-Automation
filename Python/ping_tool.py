import tkinter as tk
import subprocess


def ping():
    cmd = ["ping", entry.get(), "-n", "2"]
    output = subprocess.check_output(cmd)

    print('>', output)
    # put result in label
    result['text'] = output.decode('utf-8')

root = tk.Tk()
entry = tk.StringVar()


root.geometry('700x400')
root.title("Sys Admin Py Ping Tool")

tk.Label(root, text="Enter target IP or host as required.").pack(pady=20)
tk.Entry(root, textvariable=entry).pack(pady=10)
tk.Button(root,text="Ping Test", command=ping).pack(pady=10)
# label for ping result
result = tk.Label(root)
result.pack()

root.mainloop()