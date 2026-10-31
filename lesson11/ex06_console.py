# درس ۱۱: مدیریت خطا، منو و لغزنده
# مثال ۶: فایل ناموجود

try:
    with open('missing.txt', 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print('فایل پیدا نشد')
