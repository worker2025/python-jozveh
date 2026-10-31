# درس ۶: حلقه‌ها
# مثال ۱۱: جدول ضرب در Listbox

import tkinter as tk

win = tk.Tk()
win.title('جدول ضرب')
win.geometry('240x300')
lb = tk.Listbox(win, width=22, height=11)
lb.pack(padx=20, pady=20)
n = 7
for i in range(1, 11):
    lb.insert(tk.END, f'{n} x {i} = {n * i}')
win.mainloop()
