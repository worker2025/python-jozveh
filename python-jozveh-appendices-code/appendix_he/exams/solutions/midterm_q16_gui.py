# پیوست ح: آزمون میان‌ترم - سؤال ۱۶ (نمونه پاسخ)

import tkinter as tk

win = tk.Tk()
win.title('زوج یا فرد')
entry = tk.Entry(win)
entry.pack(pady=10)
lbl = tk.Label(win, text='', font=('Tahoma', 14))
lbl.pack()

def check():
    n = int(entry.get())
    if n % 2 == 0:
        lbl.config(text='زوج', fg='green')
    else:
        lbl.config(text='فرد', fg='red')

tk.Button(win, text='بررسی', command=check).pack(pady=10)
win.mainloop()
