# درس ۵: تصمیم‌گیری با if
# مثال ۱۰: کارنامه با چند حالت

import tkinter as tk

win = tk.Tk()
win.title('کارنامه')
win.geometry('260x200')
entry = tk.Entry(win)
entry.pack(pady=10)
lbl = tk.Label(win, text='', font=('Tahoma', 16))
lbl.pack(pady=5)

def check():
    s = float(entry.get())
    if s >= 17:
        lbl.config(text='عالی', fg='darkgreen')
    elif s >= 14:
        lbl.config(text='خوب', fg='blue')
    elif s >= 10:
        lbl.config(text='قبول', fg='orange')
    else:
        lbl.config(text='مردود', fg='red')

tk.Button(win, text='بررسی', command=check).pack()
win.mainloop()
