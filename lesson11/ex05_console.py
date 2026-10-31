# درس ۱۱: مدیریت خطا، منو و لغزنده
# مثال ۵: تکرار تا ورودی درست

while True:
    try:
        age = int(input('سن: '))
        break
    except ValueError:
        print('دوباره، فقط عدد!')
print('سن شما', age)
