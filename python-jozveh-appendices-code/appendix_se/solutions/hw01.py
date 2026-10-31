# پیوست ث: حل تمرین ۱

import tkinter as tk

win = tk.Tk()
win.title('ورود')
tk.Label(win, text='نام کاربری:').grid(row=0, column=1, sticky='e', padx=8, pady=6)
user = tk.Entry(win)
user.grid(row=0, column=0, padx=8, pady=6)
tk.Label(win, text='رمز عبور:').grid(row=1, column=1, sticky='e', padx=8, pady=6)
pwd = tk.Entry(win, show='*')
pwd.grid(row=1, column=0, padx=8, pady=6)
tk.Button(win, text='ورود', width=14).grid(row=2, column=0, columnspan=2, pady=10)
win.mainloop()
