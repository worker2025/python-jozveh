# درس ۱۱: مدیریت خطا، منو و لغزنده
# مثال ۱۲: لغزنده (Scale) (اسنیپت tirS)

import tkinter as tk

win = tk.Tk()
win.title('لغزنده')
win.geometry('300x200')
scale = tk.Scale(win, from_=0, to=100, orient='horizontal', length=220)
scale.pack(pady=15)
out = tk.Label(win, text='مقدار: 0', font=('Tahoma', 14))
out.pack()

def show(value):
    out.config(text=f'مقدار: {value}')

scale.config(command=show)
win.mainloop()
