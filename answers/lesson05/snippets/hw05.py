# تکه کد: حل تمرین ۵ درس ۵: هشدار برای کادر خالی
# این فایل مستقل اجرا نمی‌شود؛ آن را به مثال مربوط در کتاب اضافه کنید.

def login():
    if e_user.get() == '':
        messagebox.showwarning('توجه', 'نام کاربری را وارد کنید')
    elif e_user.get() == 'ali' and e_pass.get() == '1234':
        messagebox.showinfo('ورود', 'خوش آمدید')
    else:
        messagebox.showerror('خطا', 'نام کاربری یا رمز اشتباه است')
