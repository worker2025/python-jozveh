# پیوست ح: آزمون پایان‌ترم - سؤال ۱۶ (نمونه پاسخ)

import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title('ثبت‌نام')
win.geometry('280x200')
tk.Label(win, text='نام:').pack(pady=5)
entry = tk.Entry(win)
entry.pack()
news = tk.BooleanVar()
tk.Checkbutton(win, text='عضویت در خبرنامه', variable=news).pack(pady=5)

def register():
    name = entry.get().strip()
    if not name:
        messagebox.showwarning('توجه', 'نام را وارد کنید')
        return
    with open('registrations.txt', 'a', encoding='utf-8') as f:
        f.write(f'{name} - خبرنامه: {"بله" if news.get() else "خیر"}\n')
    messagebox.showinfo('ثبت', 'ثبت شد')

tk.Button(win, text='ثبت', command=register).pack(pady=10)
win.mainloop()
