# پیوست ث: مثال ۲: فرم ثبت‌نام با grid

import tkinter as tk

win = tk.Tk()
win.title('ثبت‌نام')
labels = ['نام:', 'نام خانوادگی:', 'ایمیل:']
entries = []
for r, text in enumerate(labels):
    tk.Label(win, text=text).grid(row=r, column=1, sticky='e', padx=8, pady=5)
    e = tk.Entry(win, width=24)
    e.grid(row=r, column=0, padx=8, pady=5)
    entries.append(e)
tk.Button(win, text='ثبت', width=12).grid(row=3, column=0, columnspan=2, pady=10)
win.mainloop()
