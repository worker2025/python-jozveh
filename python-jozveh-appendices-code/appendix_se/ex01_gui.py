# پیوست ث: مثال ۱: چیدمان کلاسیک با pack

import tkinter as tk

win = tk.Tk()
win.title('pack')
win.geometry('360x240')
tk.Label(win, text='نوار بالا', bg='lightblue').pack(fill='x')
tk.Label(win, text='نوار پایین', bg='lightgreen').pack(side='bottom', fill='x')
tk.Label(win, text='چپ', bg='khaki', width=10).pack(side='left', fill='y')
tk.Label(win, text='مرکز', bg='white').pack(expand=True, fill='both')
win.mainloop()
