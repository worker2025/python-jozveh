# تکه کد: حل تمرین ۵ درس ۷: حذف همه
# این فایل مستقل اجرا نمی‌شود؛ آن را به مثال مربوط در کتاب اضافه کنید.

def clear_all():
    lb.delete(0, tk.END)

tk.Button(win, text='حذف همه', command=clear_all).pack(pady=3)
