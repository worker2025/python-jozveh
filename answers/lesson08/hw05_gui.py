# درس ۸: حل تمرین ۵: اول است یا نه

import tkinter as tk

def is_prime(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

win = tk.Tk()
win.geometry('260x180')
entry = tk.Entry(win)
entry.pack(pady=10)
out = tk.Label(win, text='', font=('Tahoma', 14))
out.pack()

def check():
    if is_prime(int(entry.get())):
        out.config(text='اول است', fg='green')
    else:
        out.config(text='اول نیست', fg='red')

tk.Button(win, text='بررسی', command=check).pack(pady=10)
win.mainloop()
