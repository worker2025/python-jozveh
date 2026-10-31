# پروژه ۱: دفترچه کارها (نسخه گرافیکی)

import tkinter as tk
from tkinter import messagebox

FILE = 'tasks.txt'
win = tk.Tk()
win.title('کارهای من')
top = tk.Frame(win)
top.pack(pady=8)
entry = tk.Entry(top, width=25)
entry.pack(side='left')
lb = tk.Listbox(win, width=40)
lb.pack(padx=10, pady=10)

def save():
    with open(FILE, 'w', encoding='utf-8') as f:
        for t in lb.get(0, tk.END):
            print(t, file=f)

def add():
    if entry.get().strip():
        lb.insert(tk.END, entry.get())
        entry.delete(0, tk.END)
        save()
    else:
        messagebox.showwarning('توجه', 'متن خالی است')

def remove():
    sel = lb.curselection()
    if sel:
        lb.delete(sel[0])
        save()

tk.Button(top, text='افزودن', command=add).pack(side='left')
tk.Button(top, text='حذف', command=remove).pack(side='left')

try:
    with open(FILE, 'r', encoding='utf-8') as f:
        for line in f:
            lb.insert(tk.END, line.strip())
except FileNotFoundError:
    pass

win.mainloop()
