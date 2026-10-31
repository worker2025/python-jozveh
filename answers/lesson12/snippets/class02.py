# تکه کد (خط افزودنی): تمرین کلاسی ۲ درس ۱۲
# این فایل مستقل اجرا نمی‌شود؛ آن را به برنامه درس اضافه کنید.

def new_game():
    global secret, tries
    secret = random.randint(1, 100)
    tries = 0
    msg.config(text='', fg='black')
    entry.delete(0, tk.END)

tk.Button(win, text='بازی جدید', command=new_game).pack(pady=5)
