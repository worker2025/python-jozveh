# درس ۵: تصمیم‌گیری با if
# مثال ۹: نمره در پنجره با رنگ

import tkinter as tk

win = tk.Tk()
win.title('نمره')
win.geometry('260x200')
entry = tk.Entry(win)
entry.pack(pady=10)
lbl = tk.Label(win, text='', font=('Tahoma', 16))
lbl.pack(pady=5)

def check():
    score = float(entry.get())
    if score >= 10:
        lbl.config(text='قبول', fg='green')
    else:
        lbl.config(text='مردود', fg='red')

tk.Button(win, text='بررسی', command=check).pack()
win.mainloop()
