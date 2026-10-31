# درس ۱۰: کار با فایل
# مثال ۷: ذخیره لیست در فایل

scores = [18, 15, 20, 12]
with open('scores.txt', 'w', encoding='utf-8') as f:
    for s in scores:
        f.write(str(s) + '\n')
