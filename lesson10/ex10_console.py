# درس ۱۰: کار با فایل
# مثال ۱۰: دفتر ثبت (لاگ) ورودی‌ها

text = input('یادداشت امروز: ')
with open('diary.txt', 'a', encoding='utf-8') as f:
    f.write(text + '\n')
print('ثبت شد')
