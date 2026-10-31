# درس ۱۰: کار با فایل
# مثال ۱: نوشتن در فایل (اسنیپت izehwritefile)

with open('note.txt', 'w', encoding='utf-8') as f:
    f.write('این یک یادداشت است')
print('ذخیره شد')
