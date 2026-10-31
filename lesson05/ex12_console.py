# درس ۵: تصمیم‌گیری با if
# مثال ۱۲: ساعت و پیام روز

hour = int(input('ساعت (۰ تا ۲۳): '))
if hour < 12:
    print('صبح بخیر')
elif hour < 18:
    print('ظهر بخیر')
else:
    print('شب بخیر')
