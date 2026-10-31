# درس ۱۱: حل تمرین ۵: تغییر اندازه فونت

import tkinter as tk

win = tk.Tk()
win.geometry('360x240')
lbl = tk.Label(win, text='سلام', font=('Tahoma', 8))
lbl.pack(pady=20)

def resize(value):
    lbl.config(font=('Tahoma', int(value)))

tk.Scale(win, from_=8, to=40, orient='horizontal', length=260,
         command=resize).pack()
win.mainloop()
