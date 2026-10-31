# درس ۹: دیکشنری، تاپل و انتخاب‌ها
# مثال ۱۲: دفترچه تلفن گرافیکی

import tkinter as tk
from tkinter import messagebox

book = {'علی': '0912', 'سارا': '0935'}

win = tk.Tk()
win.title('دفترچه تلفن')
win.geometry('280x320')
tk.Label(win, text='نام:').pack()
e_name = tk.Entry(win)
e_name.pack()
tk.Label(win, text='شماره:').pack()
e_num = tk.Entry(win)
e_num.pack()
lb = tk.Listbox(win)
lb.pack(pady=8)

def refresh():
    lb.delete(0, tk.END)
    for name, num in book.items():
        lb.insert(tk.END, f'{name}: {num}')

def add():
    book[e_name.get()] = e_num.get()
    refresh()

def find():
    num = book.get(e_name.get())
    if num:
        messagebox.showinfo('نتیجه', num)
    else:
        messagebox.showwarning('نتیجه', 'پیدا نشد')

tk.Button(win, text='افزودن', command=add).pack(side='left', padx=30)
tk.Button(win, text='جستجو', command=find).pack(side='left')
refresh()
win.mainloop()
