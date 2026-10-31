# درس ۳: حل تمرین ۶: اسکناس‌ها

money = int(input('مبلغ: '))
n50 = money // 50000
money = money % 50000
n10 = money // 10000
money = money % 10000
n5 = money // 5000
money = money % 5000
print(n50, 'اسکناس ۵۰۰۰۰،', n10, 'اسکناس ۱۰۰۰۰،', n5, 'اسکناس ۵۰۰۰')
print('باقی‌مانده:', money)
