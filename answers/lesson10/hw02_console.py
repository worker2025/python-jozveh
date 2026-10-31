# درس ۱۰: حل تمرین ۲: شمارش خط

with open('names.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print('تعداد خط:', len(lines))
