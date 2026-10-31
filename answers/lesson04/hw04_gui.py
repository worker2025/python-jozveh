# درس ۴: حل تمرین ۴: پیام خوشامد

import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.geometry('280x220')
tk.Label(win, text='نام:').pack()
e1 = tk.Entry(win)
e1.pack()
tk.Label(win, text='نام خانوادگی:').pack()
e2 = tk.Entry(win)
e2.pack()

def hello():
    messagebox.showinfo('سلام', f'سلام {e1.get()} {e2.get()} عزیز')

tk.Button(win, text='سلام', command=hello).pack(pady=10)
win.mainloop()
