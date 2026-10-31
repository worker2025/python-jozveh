# درس ۹: حل تمرین ۴: فرم ثبت‌نام

import tkinter as tk

win = tk.Tk()
win.geometry('260x240')
gender = tk.StringVar(value='پسر')
news = tk.BooleanVar()
tk.Radiobutton(win, text='پسر', variable=gender, value='پسر').pack()
tk.Radiobutton(win, text='دختر', variable=gender, value='دختر').pack()
tk.Checkbutton(win, text='ثبت‌نام خبرنامه', variable=news).pack()
out = tk.Label(win, text='')
out.pack(pady=10)

def done():
    out.config(text=f'{gender.get()} - خبرنامه: {"بله" if news.get() else "خیر"}')

tk.Button(win, text='ثبت', command=done).pack()
win.mainloop()
