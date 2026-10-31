# درس ۱۰: کار با فایل
# مثال ۶: اضافه کردن به انتهای فایل

with open('names.txt', 'a', encoding='utf-8') as f:
    f.write('مریم\n')

with open('names.txt', 'r', encoding='utf-8') as f:
    print(f.read())
