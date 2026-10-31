# درس ۱۰: کار با فایل
# مثال ۱۳: شمارنده کلمه برای فایل

with open('diary.txt', 'r', encoding='utf-8') as f:
    text = f.read()
print('تعداد حروف:', len(text))
print('تعداد کلمه:', len(text.split()))
print('تعداد خط:', len(text.splitlines()))
