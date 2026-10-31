# درس ۲: متغیر و دریافت ورودی
# مثال ۱۰: محاسبه سن سال بعد در پنجره

import tkinter as tk

win = tk.Tk()
win.geometry('280x180')
tk.Label(win, text='سن شما:').pack(pady=5)
e_age = tk.Entry(win)
e_age.pack()
out = tk.Label(win, text='')
out.pack(pady=10)

def next_year():
    age = int(e_age.get())
    out.config(text=f'سال بعد {age + 1} ساله می‌شوید')

tk.Button(win, text='محاسبه', command=next_year).pack()
win.mainloop()
