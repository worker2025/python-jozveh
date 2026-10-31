# درس ۸: تابع‌ها
# مثال ۱۰: یک تابع، دو برنامه

import tkinter as tk

def area(w, h):
    return w * h

win = tk.Tk()
win.title('مساحت')
win.geometry('260x220')
tk.Label(win, text='عرض:').pack()
w = tk.Entry(win)
w.pack()
tk.Label(win, text='طول:').pack()
h = tk.Entry(win)
h.pack()
out = tk.Label(win, text='')
out.pack(pady=10)

def show():
    out.config(text=area(float(w.get()), float(h.get())))

tk.Button(win, text='مساحت', command=show).pack()
win.mainloop()
