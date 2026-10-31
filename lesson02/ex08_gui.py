# درس ۲: متغیر و دریافت ورودی
# مثال ۸: اولین ورودی گرافیکی

import tkinter as tk

win = tk.Tk()
win.title('سلام')
win.geometry('280x180')

tk.Label(win, text='نام شما:').pack(pady=5)
entry = tk.Entry(win)
entry.pack()
result = tk.Label(win, text='', font=('Tahoma', 12))
result.pack(pady=10)

def greet():
    result.config(text='سلام ' + entry.get())

tk.Button(win, text='سلام کن', command=greet).pack()
win.mainloop()
