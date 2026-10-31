# درس ۱۰: حل تمرین ۳: مرتب‌سازی نام‌ها

with open('names.txt', 'r', encoding='utf-8') as f:
    names = f.read().splitlines()
names.sort()
with open('sorted.txt', 'w', encoding='utf-8') as f:
    for n in names:
        f.write(n + '\n')
print('ذخیره شد')
