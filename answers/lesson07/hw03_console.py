# درس ۷: حل تمرین ۳: بالای میانگین

grades = [12, 18, 15, 20, 9, 17]
avg = sum(grades) / len(grades)
count = 0
for g in grades:
    if g > avg:
        count += 1
print('میانگین:', avg)
print('تعداد بالای میانگین:', count)
