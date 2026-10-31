# درس ۸: تابع‌ها
# مثال ۱۱: تغییر رنگ پنجره با پارامتر

import tkinter as tk

win = tk.Tk()
win.title('رنگ‌ها')
win.geometry('300x200')

def paint(color):
    win.config(bg=color)

tk.Button(win, text='قرمز', command=lambda: paint('tomato')).pack(pady=5)
tk.Button(win, text='سبز', command=lambda: paint('lightgreen')).pack(pady=5)
tk.Button(win, text='آبی', command=lambda: paint('lightblue')).pack(pady=5)
win.mainloop()
