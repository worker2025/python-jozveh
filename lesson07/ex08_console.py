# درس ۷: لیست‌ها
# مثال ۸: جستجو در لیست

names = ['علی', 'سارا', 'رضا']
name = input('نام: ')
if name in names:
    print('در لیست هست، جایگاه:', names.index(name))
else:
    print('در لیست نیست')
