# درس ۹: دیکشنری، تاپل و انتخاب‌ها
# مثال ۱۱: لیست کشویی (Combobox)

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('شهر')
win.geometry('260x160')
cities = ['تهران', 'شیراز', 'اصفهان', 'تبریز']
combo = ttk.Combobox(win, values=cities, state='readonly')
combo.current(0)
combo.pack(pady=15)
out = tk.Label(win, text='')
out.pack()

def show():
    out.config(text='شهر: ' + combo.get())

tk.Button(win, text='نمایش', command=show).pack(pady=10)
win.mainloop()
