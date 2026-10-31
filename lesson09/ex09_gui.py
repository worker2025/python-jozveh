# درس ۹: دیکشنری، تاپل و انتخاب‌ها
# مثال ۹: انتخاب یکی از چند گزینه (Radiobutton)

import tkinter as tk

win = tk.Tk()
win.title('سطح')
win.geometry('260x240')
level = tk.StringVar(value='آسان')

tk.Label(win, text='سطح بازی را انتخاب کنید:').pack(pady=5)
for t in ['آسان', 'متوسط', 'سخت']:
    tk.Radiobutton(win, text=t, variable=level, value=t).pack()
out = tk.Label(win, text='')
out.pack(pady=10)

def ok():
    out.config(text='انتخاب شما: ' + level.get())

tk.Button(win, text='تایید', command=ok).pack()
win.mainloop()
