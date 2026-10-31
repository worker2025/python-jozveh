# درس ۷: لیست‌ها
# مثال ۱۳: قرعه‌کشی

import random
import tkinter as tk

win = tk.Tk()
win.title('قرعه‌کشی')
win.geometry('280x240')
names = ['علی', 'سارا', 'رضا', 'مریم', 'نگین']
lbl = tk.Label(win, text='؟', font=('Tahoma', 28))
lbl.pack(pady=30)

def draw():
    lbl.config(text=random.choice(names))

tk.Button(win, text='قرعه بکش', command=draw).pack()
win.mainloop()
