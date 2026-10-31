# تکه کد: حل تمرین ۵ درس ۹: دکمه حذف
# این فایل مستقل اجرا نمی‌شود؛ آن را به مثال مربوط در کتاب اضافه کنید.

def remove():
    name = e_name.get()
    if name in book:
        del book[name]
        refresh()
    else:
        messagebox.showwarning('توجه', 'این نام نیست')

tk.Button(win, text='حذف', command=remove).pack(side='left', padx=5)
