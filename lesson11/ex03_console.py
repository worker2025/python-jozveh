# درس ۱۱: مدیریت خطا، منو و لغزنده
# مثال ۳: چند نوع خطا

try:
    a = int(input('عدد اول: '))
    b = int(input('عدد دوم: '))
    print(a / b)
except ValueError:
    print('لطفاً عدد وارد کنید')
except ZeroDivisionError:
    print('تقسیم بر صفر ممکن نیست')
