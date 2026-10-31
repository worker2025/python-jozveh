# پیوست ث: مثال ۳: پنجره‌ای که با تغییر اندازه، می‌کشد

import tkinter as tk

win = tk.Tk()
win.title('کشسان')
win.geometry('320x200')
win.columnconfigure(0, weight=1)
win.rowconfigure(1, weight=1)
tk.Entry(win).grid(row=0, column=0, sticky='ew', padx=8, pady=8)
tk.Text(win, height=5).grid(row=1, column=0, sticky='nsew', padx=8)
tk.Button(win, text='ارسال').grid(row=2, column=0, pady=8)
win.mainloop()
