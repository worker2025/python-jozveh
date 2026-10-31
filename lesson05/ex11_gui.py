# درس ۵: تصمیم‌گیری با if
# مثال ۱۱: فرم ورود

import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title('ورود')
win.geometry('260x220')
tk.Label(win, text='نام کاربری:').pack()
e_user = tk.Entry(win)
e_user.pack()
tk.Label(win, text='رمز عبور:').pack()
e_pass = tk.Entry(win, show='*')
e_pass.pack()

def login():
    if e_user.get() == 'ali' and e_pass.get() == '1234':
        messagebox.showinfo('ورود', 'خوش آمدید')
    else:
        messagebox.showerror('خطا', 'نام کاربری یا رمز اشتباه است')

tk.Button(win, text='ورود', command=login).pack(pady=12)
win.mainloop()
