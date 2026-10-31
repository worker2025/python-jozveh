# درس ۱۰: کار با فایل
# مثال ۴: خواندن خط‌به‌خط

with open('names.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())
