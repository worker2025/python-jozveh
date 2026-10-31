# پیوست پ: مثال ۴: چند روز تا امتحان؟

from datetime import date

today = date(2026, 10, 30)
exam = date(2027, 1, 15)
print((exam - today).days, 'روز مانده')
print(exam.year, exam.month, exam.day)
