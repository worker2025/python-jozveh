# درس ۲: متغیر و دریافت ورودی
# مثال ۹: دو ورودی و جمله ساختن

import tkinter as tk

win = tk.Tk()
win.title('معرفی')
win.geometry('300x240')

tk.Label(win, text='نام:').pack()
e_name = tk.Entry(win)
e_name.pack()
tk.Label(win, text='شهر:').pack()
e_city = tk.Entry(win)
e_city.pack()
out = tk.Label(win, text='')
out.pack(pady=10)

def show():
    out.config(text=e_name.get() + ' اهل ' + e_city.get() + ' است')

tk.Button(win, text='نمایش', command=show).pack()
win.mainloop()
