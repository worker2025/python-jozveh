# درس ۷: لیست‌ها
# مثال ۱۲: مرتب‌سازی و شمارش

import tkinter as tk

win = tk.Tk()
win.geometry('300x380')
entry = tk.Entry(win)
entry.pack(pady=8)
lb = tk.Listbox(win)
lb.pack(pady=5)
info = tk.Label(win, text='تعداد: 0')
info.pack()

def add():
    lb.insert(tk.END, entry.get())
    entry.delete(0, tk.END)
    info.config(text=f'تعداد: {lb.size()}')

def sort_list():
    items = sorted(lb.get(0, tk.END))
    lb.delete(0, tk.END)
    for it in items:
        lb.insert(tk.END, it)

tk.Button(win, text='افزودن', command=add).pack(pady=3)
tk.Button(win, text='مرتب‌سازی', command=sort_list).pack(pady=3)
win.mainloop()
