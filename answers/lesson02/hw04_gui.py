# درس ۲: حل تمرین ۴: سلام و پاک کردن

import tkinter as tk

win = tk.Tk()
win.geometry('280x200')
entry = tk.Entry(win)
entry.pack(pady=10)
out = tk.Label(win, text='')
out.pack()

def hello():
    out.config(text='خوش آمدید ' + entry.get())

def clear():
    entry.delete(0, tk.END)
    out.config(text='')

tk.Button(win, text='سلام', command=hello).pack(pady=5)
tk.Button(win, text='پاک کردن', command=clear).pack()
win.mainloop()
