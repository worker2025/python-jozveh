# درس ۱۱: مدیریت خطا، منو و لغزنده
# مثال ۴: else و finally

try:
    n = int(input('عدد: '))
except ValueError:
    print('نامعتبر')
else:
    print('عدد معتبر بود:', n)
finally:
    print('پایان بررسی')
