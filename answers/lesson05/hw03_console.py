# درس ۵: حل تمرین ۳: نوع مثلث

a = float(input('ضلع اول: '))
b = float(input('ضلع دوم: '))
c = float(input('ضلع سوم: '))
if a == b and b == c:
    print('متساوی‌الاضلاع')
elif a == b or b == c or a == c:
    print('متساوی‌الساقین')
else:
    print('مختلف‌الاضلاع')
