# درس ۹: دیکشنری، تاپل و انتخاب‌ها
# مثال ۱۰: گزینه بله/خیر (Checkbutton)

import tkinter as tk

win = tk.Tk()
win.title('سفارش')
win.geometry('260x260')
pizza = tk.BooleanVar()
drink = tk.BooleanVar()
salad = tk.BooleanVar()

tk.Checkbutton(win, text='پیتزا', variable=pizza).pack(anchor='w', padx=20)
tk.Checkbutton(win, text='نوشابه', variable=drink).pack(anchor='w', padx=20)
tk.Checkbutton(win, text='سالاد', variable=salad).pack(anchor='w', padx=20)
out = tk.Label(win, text='')
out.pack(pady=10)

def order():
    items = []
    if pizza.get():
        items.append('پیتزا')
    if drink.get():
        items.append('نوشابه')
    if salad.get():
        items.append('سالاد')
    out.config(text='سفارش: ' + ('، '.join(items) if items else 'خالی'))

tk.Button(win, text='ثبت سفارش', command=order).pack()
win.mainloop()
