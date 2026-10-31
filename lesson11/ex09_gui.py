# درس ۱۱: مدیریت خطا، منو و لغزنده
# مثال ۹: ماشین‌حساب گرافیکی ایمن

import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title('تقسیم')
win.geometry('260x200')
e1 = tk.Entry(win)
e1.pack(pady=8)
e2 = tk.Entry(win)
e2.pack()

def divide():
    try:
        r = float(e1.get()) / float(e2.get())
        messagebox.showinfo('نتیجه', r)
    except ValueError:
        messagebox.showerror('خطا', 'لطفاً عدد وارد کنید')
    except ZeroDivisionError:
        messagebox.showerror('خطا', 'تقسیم بر صفر ممکن نیست')

tk.Button(win, text='تقسیم', command=divide).pack(pady=12)
win.mainloop()
