# درس ۷: حل تمرین ۴: حذف تکراری‌ها

items = [3, 5, 3, 7, 5, 9]
unique = []
for x in items:
    if x not in unique:
        unique.append(x)
print(unique)
