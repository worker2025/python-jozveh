# درس ۱: حل تمرین ۳: سه برچسب رنگی

import tkinter as tk

win = tk.Tk()
win.geometry('300x200')
win.config(bg='#fff3e0')
tk.Label(win, text='قرمز', fg='red', bg='#fff3e0').pack(pady=8)
tk.Label(win, text='سبز', fg='green', bg='#fff3e0').pack(pady=8)
tk.Label(win, text='آبی', fg='blue', bg='#fff3e0').pack(pady=8)
win.mainloop()
