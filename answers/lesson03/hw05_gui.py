# درس ۳: حل تمرین ۵: وتر مثلث

import math
import tkinter as tk

win = tk.Tk()
win.geometry('280x240')
tk.Label(win, text='ضلع اول:').pack()
e1 = tk.Entry(win)
e1.pack()
tk.Label(win, text='ضلع دوم:').pack()
e2 = tk.Entry(win)
e2.pack()
out = tk.Label(win, text='')
out.pack(pady=10)

def calc():
    a = float(e1.get())
    b = float(e2.get())
    out.config(text=f'وتر: {math.sqrt(a ** 2 + b ** 2):.2f}')

tk.Button(win, text='محاسبه', command=calc).pack()
win.mainloop()
