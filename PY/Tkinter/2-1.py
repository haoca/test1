import tkinter as tk

window = tk.Tk()
window.title('计算器')

window.geometry('400x400')
window.grid()
l = tk.Label(window, text='NO.1', anchor='w',
             font=('Arial', 12))
# l.pack()
l.grid(row=0, column=0)
e1 = tk.Entry(window, show=None)

# e1.pack()
e1.grid(row=1, column=0)
l = tk.Label(window, text='NO.2',
             font=('Arial', 12))
# l.pack()
l.grid(row=2, column=0)
e2 = tk.Entry(window, show=None)
# e2.pack()
e2.grid(row=3, column=0)


def plus():
    try:
        if e1.get() == '':
            print('worry')
        c = int(e1.get())+int(e2.get())

        var.set(c)
    except:
        pass


def clear():
    e1.delete(0, 9999999)
    e2.delete(0, 9999999)


b1 = tk.Button(window, text='plus', width=15,
               height=2, command=plus)
# b1.pack()
b1.grid(row=4, column=0)
b2 = tk.Button(window, text='clear', width=15,
               height=2, command=clear)
# b2.pack()
b2.grid(row=5, column=0)
var = tk.StringVar()
t = tk.Label(window, textvariable=var,
             font=('Arial', 12), width=30, height=2)
# t.pack()
t.grid(row=6, column=0)
window.mainloop()
