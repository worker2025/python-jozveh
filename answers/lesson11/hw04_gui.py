# درس ۱۱: حل تمرین ۴: ماشین‌حساب ایمن

import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.geometry('300x240')
e1 = tk.Entry(win)
e1.pack(pady=5)
e2 = tk.Entry(win)
e2.pack()
out = tk.Label(win, text='نتیجه')
out.pack(pady=10)

def calc(op):
    try:
        a = float(e1.get())
        b = float(e2.get())
        if op == '+':
            out.config(text=a + b)
        elif op == '-':
            out.config(text=a - b)
        elif op == '*':
            out.config(text=a * b)
        else:
            out.config(text=a / b)
    except ValueError:
        messagebox.showerror('خطا', 'عدد وارد کنید')
    except ZeroDivisionError:
        messagebox.showerror('خطا', 'تقسیم بر صفر')

for s in ['+', '-', '*', '/']:
    tk.Button(win, text=s, width=4,
              command=lambda x=s: calc(x)).pack(side='left', padx=8)
win.mainloop()
