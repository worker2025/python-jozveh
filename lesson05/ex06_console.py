# درس ۵: تصمیم‌گیری با if
# مثال ۶: بزرگ‌ترین از سه عدد

a = float(input('عدد اول: '))
b = float(input('عدد دوم: '))
c = float(input('عدد سوم: '))

if a >= b and a >= c:
    print('بزرگ‌ترین:', a)
elif b >= c:
    print('بزرگ‌ترین:', b)
else:
    print('بزرگ‌ترین:', c)
