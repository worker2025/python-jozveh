# درس ۱۰: حل تمرین ۵: نمایش تعداد کلمه

import tkinter as tk

win = tk.Tk()
text = tk.Text(win, width=40, height=10)
text.pack(padx=10, pady=10)
info = tk.Label(win, text='کلمه‌ها: 0')
info.pack()

def count(event):
    n = len(text.get('1.0', tk.END).split())
    info.config(text=f'کلمه‌ها: {n}')

text.bind('<KeyRelease>', count)
win.mainloop()
