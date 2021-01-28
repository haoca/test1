# import tkinter as tk
from tkinter import *
root = Tk()
root.title('download')
root.geometry('560x450+350+100')
label = Label(root, text='please input songs name:')
label.grid()

var = StringVar()
r1 = Radiobutton(root, text='123', variable=var, value='456')
r1.grid(row=1, column=0)
r2 = Radiobutton(root, text='789', variable=var, value='1011')
r2.grid(row=1, column=1)
label2 = Label(root, text=var)
label2.grid()
root.mainloop()
