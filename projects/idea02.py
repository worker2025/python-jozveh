# ایده ۲: ساعت دیجیتال

import time
import tkinter as tk

win = tk.Tk()
win.title('ساعت')
win.geometry('260x120')
lbl = tk.Label(win, font=('Tahoma', 32))
lbl.pack(expand=True)

def tick():
    lbl.config(text=time.strftime('%H:%M:%S'))
    win.after(1000, tick)

tick()
win.mainloop()
