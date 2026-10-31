# درس ۱۰: کار با فایل
# مثال ۱۲: نوت‌پد با انتخاب فایل

import tkinter as tk
from tkinter import filedialog

win = tk.Tk()
win.title('نوت‌پد ساده')
text = tk.Text(win, width=50, height=15)
text.pack(padx=10, pady=10)

def save_as():
    path = filedialog.asksaveasfilename(defaultextension='.txt')
    if path:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text.get('1.0', tk.END))

def open_file():
    path = filedialog.askopenfilename(filetypes=[('متن', '*.txt')])
    if path:
        with open(path, 'r', encoding='utf-8') as f:
            text.delete('1.0', tk.END)
            text.insert('1.0', f.read())

tk.Button(win, text='باز کردن', command=open_file).pack(side='left', padx=10)
tk.Button(win, text='ذخیره', command=save_as).pack(side='left')
win.mainloop()
