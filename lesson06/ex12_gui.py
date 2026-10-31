# درس ۶: حلقه‌ها
# مثال ۱۲: جدول ضرب با عدد دلخواه

import tkinter as tk

win = tk.Tk()
win.title('جدول ضرب')
win.geometry('260x380')
entry = tk.Entry(win, width=10)
entry.pack(pady=10)
lb = tk.Listbox(win, width=22, height=11)
lb.pack(padx=20, pady=10)

def make():
    lb.delete(0, tk.END)
    n = int(entry.get())
    for i in range(1, 11):
        lb.insert(tk.END, f'{n} x {i} = {n * i}')

tk.Button(win, text='بساز', command=make).pack()
win.mainloop()
