# پیوست ت: حل برنامه معیوب ۴

import tkinter as tk

win = tk.Tk()
lbl = tk.Label(win, text='کلیک نشده')
lbl.pack()

def clicked():
    lbl.config(text='کلیک شد')

tk.Button(win, text='کلیک', command=clicked).pack()
win.mainloop()
