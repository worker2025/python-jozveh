# پروژه ۴: دفتر نمره‌ها

import tkinter as tk
from tkinter import messagebox

grades = []

win = tk.Tk()
win.title('دفتر نمره')
win.geometry('300x380')
entry = tk.Entry(win)
entry.pack(pady=8)
lb = tk.Listbox(win, height=8)
lb.pack()
info = tk.Label(win, text='', font=('Tahoma', 11))
info.pack(pady=10)

def refresh():
    if grades:
        avg = sum(grades) / len(grades)
        info.config(text=f'میانگین: {avg:.2f}\nبیشترین: {max(grades)} - کمترین: {min(grades)}')
    else:
        info.config(text='')

def add():
    try:
        g = float(entry.get())
        if not 0 <= g <= 20:
            raise ValueError
    except ValueError:
        messagebox.showerror('خطا', 'نمره باید عددی بین ۰ تا ۲۰ باشد')
        return
    grades.append(g)
    lb.insert(tk.END, g)
    entry.delete(0, tk.END)
    refresh()

tk.Button(win, text='افزودن نمره', command=add).pack()
win.mainloop()
