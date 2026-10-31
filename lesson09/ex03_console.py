# درس ۹: دیکشنری، تاپل و انتخاب‌ها
# مثال ۳: پیمایش دیکشنری

student = {'نام': 'سارا', 'سن': 15, 'نمره': 19}
for key in student:
    print(key)
for value in student.values():
    print(value)
for key, value in student.items():
    print(key, ':', value)
