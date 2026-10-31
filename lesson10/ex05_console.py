# درس ۱۰: کار با فایل
# مثال ۵: خواندن به شکل لیست

with open('names.txt', 'r', encoding='utf-8') as f:
    names = f.read().splitlines()
print(names)
print(len(names), 'نام در فایل است')
