# درس ۹: حل تمرین ۶: مترجم ساده

import tkinter as tk
from tkinter import ttk

words = {'apple': 'سیب', 'book': 'کتاب', 'cat': 'گربه',
         'water': 'آب', 'sun': 'خورشید'}

win = tk.Tk()
win.geometry('260x180')
combo = ttk.Combobox(win, values=list(words.keys()), state='readonly')
combo.current(0)
combo.pack(pady=15)
out = tk.Label(win, text='', font=('Tahoma', 14))
out.pack()

def translate():
    out.config(text=words[combo.get()])

tk.Button(win, text='ترجمه', command=translate).pack(pady=10)
win.mainloop()
