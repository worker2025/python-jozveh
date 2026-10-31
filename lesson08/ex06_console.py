# درس ۸: تابع‌ها
# مثال ۶: تابع با شرط

def grade(score):
    if score >= 17:
        return 'عالی'
    elif score >= 10:
        return 'قبول'
    return 'مردود'

print(grade(18))
print(grade(12))
print(grade(7))
