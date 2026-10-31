# درس ۱۱: حل تمرین ۶: نوت‌پد با منوی کامل

import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title('نوت‌پد')
text = tk.Text(win, width=50, height=15)
text.pack(padx=10, pady=10)

def new():
    text.delete('1.0', tk.END)

def save():
    with open('note.txt', 'w', encoding='utf-8') as f:
        f.write(text.get('1.0', tk.END))

def load():
    try:
        with open('note.txt', 'r', encoding='utf-8') as f:
            text.delete('1.0', tk.END)
            text.insert('1.0', f.read())
    except FileNotFoundError:
        messagebox.showwarning('توجه', 'فایلی برای باز کردن نیست')

menubar = tk.Menu(win)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='جدید', command=new)
filemenu.add_command(label='باز کردن', command=load)
filemenu.add_command(label='ذخیره', command=save)
filemenu.add_separator()
filemenu.add_command(label='خروج', command=win.destroy)
menubar.add_cascade(label='فایل', menu=filemenu)
win.config(menu=menubar)
win.mainloop()
