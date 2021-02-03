import tkinter as tk

window = tk.Tk()
window.title('计算器')

window.geometry('400x300')

var = tk.StringVar()
l = tk.Label(window, textvariable=var,
             font=('Arial', 12), width=30, height=2)
l.pack()
on_hit = False


def hit_me():
    global on_hit
    print(on_hit)
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('noooooo!!!')


b = tk.Button(window, text='hit me', width=15,
              height=2, command=hit_me)
b.pack()
window.mainloop()
