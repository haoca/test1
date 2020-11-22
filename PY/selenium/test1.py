import tkinter as tk
import base64
import requests
import json
import uuid

window = tk.Tk()
window.title('校园网登陆器')

window.geometry('400x300')

L1 = tk.Label(window, text="网站名")
L1.pack()
E1 = tk.Entry(window, bd=7)
E1.pack()

window.mainloop()
