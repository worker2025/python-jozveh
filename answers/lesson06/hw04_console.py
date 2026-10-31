# درس ۶: حل تمرین ۴: جمع تا عدد منفی

total = 0
n = int(input('عدد: '))
while n >= 0:
    total += n
    n = int(input('عدد: '))
print('جمع:', total)
