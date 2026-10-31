# درس ۱۰: کار با فایل
# مثال ۲: خواندن فایل (اسنیپت izehreadfile)

with open('note.txt', 'r', encoding='utf-8') as f:
    content = f.read()
print(content)
