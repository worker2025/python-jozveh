# درس ۶: حل تمرین ۲: فاکتوریل

n = int(input('عدد: '))
f = 1
for i in range(2, n + 1):
    f *= i
print(f'{n}! = {f}')
