# درس ۱: اولین برنامه و اولین پنجره
# مثال ۷: کارت معرفی گرافیکی

import tkinter as tk

win = tk.Tk()
win.title('کارت معرفی')
win.geometry('320x220')
win.config(bg='lightyellow')

tk.Label(win, text='علی رضایی', font=('Tahoma', 18, 'bold'),
         bg='lightyellow').pack(pady=10)
tk.Label(win, text='دانش‌آموز پایتون', fg='blue',
         bg='lightyellow').pack()
tk.Label(win, text='Tirotir.ir', fg='gray',
         bg='lightyellow').pack(pady=20)
win.mainloop()
