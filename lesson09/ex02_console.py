# درس ۹: دیکشنری، تاپل و انتخاب‌ها
# مثال ۲: افزودن، تغییر و حذف

student = {'نام': 'سارا', 'سن': 15}
student['شهر'] = 'تهران'
student['سن'] = 16
print(student)
del student['شهر']
print(student)
print(len(student))
