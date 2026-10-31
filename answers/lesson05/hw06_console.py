# درس ۵: حل تمرین ۶: حدس عدد

secret = 7
guess = int(input('حدس شما: '))
if guess > secret:
    print('کوچک‌تر')
elif guess < secret:
    print('بزرگ‌تر')
else:
    print('درست حدس زدید!')
