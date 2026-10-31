# پیوست ث: مثال ۵: ترکیب ظرف‌ها

import tkinter as tk

win = tk.Tk()
win.title('ترکیب')
top = tk.Frame(win)
top.pack(pady=8)
tk.Label(top, text='نام:').pack(side='right')
entry = tk.Entry(top)
entry.pack(side='right', padx=5)

group = tk.LabelFrame(win, text='گزینه‌ها', padx=10, pady=5)
group.pack(padx=10, pady=5, fill='x')
choice = tk.StringVar(value='a')
tk.Radiobutton(group, text='گزینه اول', variable=choice, value='a').grid(row=0, column=0)
tk.Radiobutton(group, text='گزینه دوم', variable=choice, value='b').grid(row=0, column=1)

tk.Button(win, text='تایید').pack(pady=8)
win.mainloop()
