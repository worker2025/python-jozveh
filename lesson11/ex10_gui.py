# درس ۱۱: مدیریت خطا، منو و لغزنده
# مثال ۱۰: بازکردن ایمن در نوت‌پد

import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
text = tk.Text(win, width=40, height=10)
text.pack(padx=10, pady=10)

def load():
    try:
        with open('note.txt', 'r', encoding='utf-8') as f:
            text.delete('1.0', tk.END)
            text.insert('1.0', f.read())
    except FileNotFoundError:
        messagebox.showwarning('توجه', 'هنوز یادداشتی ذخیره نشده است')

def save():
    with open('note.txt', 'w', encoding='utf-8') as f:
        f.write(text.get('1.0', tk.END))

tk.Button(win, text='ذخیره', command=save).pack(side='left', padx=10)
tk.Button(win, text='باز کردن', command=load).pack(side='left')
win.mainloop()
