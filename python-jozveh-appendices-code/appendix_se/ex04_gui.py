# پیوست ث: مثال ۴: قرار دادن دقیق

import tkinter as tk

win = tk.Tk()
win.geometry('300x200')
tk.Label(win, text='وسط', bg='gold', width=10).place(relx=0.5, rely=0.5, anchor='center')
tk.Button(win, text='گوشه').place(x=10, y=10)
tk.Button(win, text='پایین راست').place(relx=1.0, rely=1.0, anchor='se')
win.mainloop()
