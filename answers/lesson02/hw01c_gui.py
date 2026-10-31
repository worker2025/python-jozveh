# درس ۲: حل تمرین ۱: محاسبه سن

import tkinter as tk

win = tk.Tk()
win.geometry('280x240')
tk.Label(win, text='عرض:').pack()
e_w = tk.Entry(win)
e_w.pack()
tk.Label(win, text='طول:').pack()
e_h = tk.Entry(win)
e_h.pack()
out = tk.Label(win, text='')
out.pack(pady=10)

def calc():
    w = float(e_w.get())
    h = float(e_h.get())
    out.config(text=f'مساحت: {w * h} - محیط: {2 * (w + h)}')

tk.Button(win, text='محاسبه', command=calc).pack()
win.mainloop()
