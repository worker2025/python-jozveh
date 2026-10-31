# درس ۴: حل تمرین ۵: شمارنده کلمه و حرف

import tkinter as tk

win = tk.Tk()
win.geometry('320x180')
entry = tk.Entry(win, width=35)
entry.pack(pady=15)
lbl = tk.Label(win, text='')
lbl.pack()

def count(event):
    t = entry.get()
    lbl.config(text=f'حروف: {len(t)} - کلمه‌ها: {len(t.split())}')

entry.bind('<KeyRelease>', count)
win.mainloop()
