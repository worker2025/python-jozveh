# پیوست ح: آزمون میان‌ترم - سؤال ۱۵ (نمونه پاسخ)

n = int(input('n: '))
total = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        total += i
print('جمع زوج‌ها:', total)
