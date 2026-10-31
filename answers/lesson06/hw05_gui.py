# درس ۶: حل تمرین ۵: فاکتوریل گرافیکی

import tkinter as tk

win = tk.Tk()
win.geometry('260x180')
entry = tk.Entry(win)
entry.pack(pady=10)
lbl = tk.Label(win, text='')
lbl.pack()

def calc():
    n = int(entry.get())
    f = 1
    for i in range(2, n + 1):
        f *= i
    lbl.config(text=f'{n}! = {f}')

tk.Button(win, text='محاسبه', command=calc).pack(pady=10)
win.mainloop()
