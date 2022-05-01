import os
import tkinter
import webbrowser
import socket

tk = tk.Tk()
tk.geometry(f'200x200')
tk.configure(bg='black')

def your_ip():
  hostname = socket.gethostname()
  local_ip = socket.gethostbyname(hostname)
  print(local_ip)
  
b1 = Button(tk, text='Click)', command=your_ip)

b1.pack()

tk.mainloop()
