# درس ۱۱: مدیریت خطا، منو و لغزنده
# مثال ۱۱: منوی پنجره (اسنیپت tirM)

import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title('منو')
win.geometry('300x200')

def about():
    messagebox.showinfo('درباره', 'برنامه آموزشی Tirotir.ir')

menubar = tk.Menu(win)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='درباره', command=about)
filemenu.add_separator()
filemenu.add_command(label='خروج', command=win.destroy)
menubar.add_cascade(label='فایل', menu=filemenu)
win.config(menu=menubar)
win.mainloop()
