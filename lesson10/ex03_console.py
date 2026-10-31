# درس ۱۰: کار با فایل
# مثال ۳: چند خط نوشتن

with open('names.txt', 'w', encoding='utf-8') as f:
    f.write('علی\n')
    f.write('سارا\n')
    f.write('رضا\n')
