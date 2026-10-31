# درس ۳: حل تمرین ۴: دایره گرافیکی

import math
import tkinter as tk

win = tk.Tk()
win.geometry('280x200')
tk.Label(win, text='شعاع:').pack()
e = tk.Entry(win)
e.pack()
out = tk.Label(win, text='')
out.pack(pady=10)

def calc():
    r = float(e.get())
    out.config(text=f'مساحت: {math.pi * r ** 2:.2f}')

tk.Button(win, text='محاسبه', command=calc).pack()
win.mainloop()
