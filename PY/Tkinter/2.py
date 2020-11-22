import tkinter as tk

window = tk.Tk()
window.title('计算器')

window.geometry('400x300')

e = tk.Entry(window, show=None)
e.pack()


def insert_point():
    var = e.get()
    t.insert('insert', var)
#  = tk.Entry(window, show='*')


def insert_end():
    var = e.get()
    t.insert('end', var)


def clear():
    e.delete(0, 99999999)


b1 = tk.Button(window, text='insert point', width=15,
               height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert end', width=15,
               height=2, command=insert_end)
b2.pack()
b2 = tk.Button(window, text='clear', width=15,
               height=2, command=clear)
b2.pack()
t = tk.Text(window, height=2)
t.pack()
window.mainloop()
