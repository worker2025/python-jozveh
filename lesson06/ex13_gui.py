# درس ۶: حلقه‌ها
# مثال ۱۳: شمارش معکوس

import tkinter as tk

win = tk.Tk()
win.geometry('240x180')
lbl = tk.Label(win, text='10', font=('Tahoma', 40))
lbl.pack(pady=20)
n = 10

def tick():
    global n
    n -= 1
    lbl.config(text=n)
    if n > 0:
        win.after(1000, tick)

win.after(1000, tick)
win.mainloop()
