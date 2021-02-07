import tkinter as tk

window = tk.Tk()
window.title('计算器')

window.geometry('400x300')

var1 = tk.StringVar()
l = tk.Label(window, bg='white', width=12,
             font=('Arial', 12), textvariable=var1)
l.pack()


def insert_point():
    var = lb.get(lb.curselection())
    var1.set(var)


b1 = tk.Button(window, text='print selection', width=15,
               height=2, command=insert_point)
b1.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))
lb = tk.Listbox(window, listvariable=var2)
list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert('end', item)
lb.insert(0, 'first')
lb.insert(1, 'second')
# lb.delete(2)
lb.pack()
window.mainloop()
