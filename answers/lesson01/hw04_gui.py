# درس ۱: حل تمرین ۴: پنجره ثابت با دو دکمه

import tkinter as tk

win = tk.Tk()
win.geometry('400x300')
win.resizable(False, False)
tk.Button(win, text='خروج', command=win.destroy).pack(pady=40)
tk.Button(win, text='دکمه دوم').pack()
win.mainloop()
