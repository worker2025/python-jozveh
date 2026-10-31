# درس ۱۱: حل تمرین ۱: جمع عددهای معتبر

total = 0
for i in range(5):
    try:
        total += float(input('عدد: '))
    except ValueError:
        print('نادیده گرفته شد')
print('جمع:', total)
