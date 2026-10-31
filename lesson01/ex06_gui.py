# درس ۱: اولین برنامه و اولین پنجره
# مثال ۶: اولین پنجره

import tkinter as tk

win = tk.Tk()
win.title('اولین پنجره')
win.geometry('300x150')
tk.Label(win, text='سلام دنیا!', font=('Tahoma', 16)).pack(pady=40)
win.mainloop()
