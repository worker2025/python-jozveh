# درس ۵: تصمیم‌گیری با if
# مثال ۵: ترکیب شرط‌ها با and و or

age = int(input('سن: '))
has_ticket = input('بلیت دارید؟ (بله/خیر) ') == 'بله'

if age >= 12 and has_ticket:
    print('وارد شوید')
elif not has_ticket:
    print('ابتدا بلیت بگیرید')
else:
    print('این فیلم برای شما مناسب نیست')
