# درس ۳: عملیات ریاضی
# مثال ۱۰: محاسبه تخفیف در پنجره

import tkinter as tk

win = tk.Tk()
win.title('تخفیف')
win.geometry('300x260')
tk.Label(win, text='قیمت (تومان):').pack()
e_price = tk.Entry(win)
e_price.pack()
tk.Label(win, text='درصد تخفیف:').pack()
e_off = tk.Entry(win)
e_off.pack()
out = tk.Label(win, text='')
out.pack(pady=10)

def calc():
    price = float(e_price.get())
    off = float(e_off.get())
    final = price - price * off / 100
    out.config(text=f'قیمت نهایی: {final:.0f} تومان')

tk.Button(win, text='محاسبه', command=calc).pack()
win.mainloop()
