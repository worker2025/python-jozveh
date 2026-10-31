# درس ۵: حل تمرین ۴: بخش‌پذیری گرافیکی

import tkinter as tk

win = tk.Tk()
win.geometry('260x180')
entry = tk.Entry(win)
entry.pack(pady=10)
lbl = tk.Label(win, text='')
lbl.pack()

def check():
    n = int(entry.get())
    if n % 3 == 0:
        lbl.config(text='بخش‌پذیر است', fg='green')
    else:
        lbl.config(text='بخش‌پذیر نیست', fg='red')

tk.Button(win, text='بررسی', command=check).pack()
win.mainloop()
