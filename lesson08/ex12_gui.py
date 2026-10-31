# درس ۸: تابع‌ها
# مثال ۱۲: ماشین‌حساب با تابع کمکی

import tkinter as tk

win = tk.Tk()
win.title('ماشین‌حساب')
win.geometry('300x280')
tk.Label(win, text='عدد اول:').pack()
e1 = tk.Entry(win)
e1.pack()
tk.Label(win, text='عدد دوم:').pack()
e2 = tk.Entry(win)
e2.pack()
out = tk.Label(win, text='نتیجه', font=('Tahoma', 14))
out.pack(pady=10)

def calc(op):
    a = float(e1.get())
    b = float(e2.get())
    if op == '+':
        out.config(text=a + b)
    elif op == '-':
        out.config(text=a - b)
    elif op == '*':
        out.config(text=a * b)
    elif op == '/':
        out.config(text=a / b)

for symbol in ['+', '-', '*', '/']:
    tk.Button(win, text=symbol, width=4,
              command=lambda s=symbol: calc(s)).pack(side='left', padx=8)
win.mainloop()
