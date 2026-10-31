# پروژه ۲: بازی حدس عدد

import random
import tkinter as tk

secret = random.randint(1, 100)
tries = 0

win = tk.Tk()
win.title('حدس عدد')
win.geometry('300x240')
tk.Label(win, text='عددی بین ۱ تا ۱۰۰ حدس بزنید').pack(pady=10)
entry = tk.Entry(win)
entry.pack()
msg = tk.Label(win, text='', font=('Tahoma', 12))
msg.pack(pady=10)

def guess():
    global tries
    try:
        g = int(entry.get())
    except ValueError:
        msg.config(text='فقط عدد!', fg='red')
        return
    tries += 1
    if g > secret:
        msg.config(text='کوچک‌تر', fg='blue')
    elif g < secret:
        msg.config(text='بزرگ‌تر', fg='blue')
    else:
        msg.config(text=f'آفرین! در {tries} حدس', fg='green')

tk.Button(win, text='حدس', command=guess).pack()
win.mainloop()
