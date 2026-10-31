# درس ۱۱: مدیریت خطا، منو و لغزنده
# مثال ۲: اولین try و except

try:
    n = int(input('یک عدد: '))
    print('دو برابر:', n * 2)
except ValueError:
    print('این عدد نیست!')
print('برنامه ادامه دارد')
