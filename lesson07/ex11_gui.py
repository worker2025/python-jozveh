# درس ۷: لیست‌ها
# مثال ۱۱: لیست خرید در پنجره (افزودن و حذف)

import tkinter as tk

win = tk.Tk()
win.title('لیست خرید')
win.geometry('300x340')
entry = tk.Entry(win)
entry.pack(pady=8)
lb = tk.Listbox(win)
lb.pack(pady=5)

def add():
    if entry.get() != '':
        lb.insert(tk.END, entry.get())
        entry.delete(0, tk.END)

def remove():
    sel = lb.curselection()
    if sel:
        lb.delete(sel[0])

tk.Button(win, text='افزودن', command=add).pack(pady=3)
tk.Button(win, text='حذف انتخاب‌شده', command=remove).pack(pady=3)
win.mainloop()
