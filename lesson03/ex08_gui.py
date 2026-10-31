# درس ۳: عملیات ریاضی
# مثال ۸: ماشین‌حساب گرافیکی با چهار دکمه

import tkinter as tk

win = tk.Tk()
win.title('ماشین‌حساب')
win.geometry('300x300')

tk.Label(win, text='عدد اول:').pack()
e1 = tk.Entry(win)
e1.pack()
tk.Label(win, text='عدد دوم:').pack()
e2 = tk.Entry(win)
e2.pack()
out = tk.Label(win, text='نتیجه', font=('Tahoma', 14))
out.pack(pady=10)

def add():
    out.config(text=float(e1.get()) + float(e2.get()))

def sub():
    out.config(text=float(e1.get()) - float(e2.get()))

def mul():
    out.config(text=float(e1.get()) * float(e2.get()))

def div():
    out.config(text=float(e1.get()) / float(e2.get()))

tk.Button(win, text='+', width=4, command=add).pack(side='left', padx=8)
tk.Button(win, text='-', width=4, command=sub).pack(side='left', padx=8)
tk.Button(win, text='×', width=4, command=mul).pack(side='left', padx=8)
tk.Button(win, text='÷', width=4, command=div).pack(side='left', padx=8)
win.mainloop()
