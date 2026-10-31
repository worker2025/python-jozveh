# درس ۱: اولین برنامه و اولین پنجره
# مثال ۹: پنجره‌ای با اندازه ثابت

import tkinter as tk

win = tk.Tk()
win.title('پنجره ثابت')
win.geometry('360x200')
win.resizable(False, False)
tk.Label(win, text='اندازه این پنجره تغییر نمی‌کند',
         font=('Tahoma', 12)).pack(expand=True)
win.mainloop()
