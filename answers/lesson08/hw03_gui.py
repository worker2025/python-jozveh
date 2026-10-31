# درس ۸: حل تمرین ۳: تبدیل دما در پنجره

import tkinter as tk

def celsius_to_f(c):
    return c * 9 / 5 + 32

win = tk.Tk()
win.geometry('260x180')
entry = tk.Entry(win)
entry.pack(pady=10)
out = tk.Label(win, text='')
out.pack()

def convert():
    out.config(text=f'{celsius_to_f(float(entry.get())):.1f} فارنهایت')

tk.Button(win, text='تبدیل', command=convert).pack(pady=10)
win.mainloop()
