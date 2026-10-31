# درس ۱۱: حل تمرین ۲: اندیس ایمن

names = ['علی', 'سارا', 'رضا']
try:
    i = int(input('اندیس: '))
    print(names[i])
except ValueError:
    print('عدد وارد کنید')
except IndexError:
    print('اندیس خارج از لیست است')
