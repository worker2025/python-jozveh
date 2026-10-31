# درس ۱: اولین برنامه و اولین پنجره
# مثال ۸: دکمه خروج

import tkinter as tk

win = tk.Tk()
win.title('خروج')
win.geometry('260x140')
tk.Label(win, text='برای بستن دکمه را بزنید').pack(pady=15)
tk.Button(win, text='خروج', command=win.destroy).pack()
win.mainloop()
