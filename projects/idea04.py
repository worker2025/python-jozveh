# ایده ۴: سنگ، کاغذ، قیچی

import random
import tkinter as tk

win = tk.Tk()
win.title('سنگ کاغذ قیچی')
win.geometry('320x220')
out = tk.Label(win, text='انتخاب کنید', font=('Tahoma', 12))
out.pack(pady=20)

def play(mine):
    pc = random.choice(['سنگ', 'کاغذ', 'قیچی'])
    wins = [('سنگ', 'قیچی'), ('کاغذ', 'سنگ'), ('قیچی', 'کاغذ')]
    if mine == pc:
        result = 'مساوی'
    elif (mine, pc) in wins:
        result = 'شما بردید'
    else:
        result = 'رایانه برد'
    out.config(text=f'شما: {mine} - رایانه: {pc}\n{result}')

for name in ['سنگ', 'کاغذ', 'قیچی']:
    tk.Button(win, text=name, width=8,
              command=lambda n=name: play(n)).pack(side='left', padx=10)
win.mainloop()
