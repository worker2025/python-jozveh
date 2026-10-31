# درس ۱۰: حل تمرین ۱: ذخیره و جمع

with open('nums.txt', 'w', encoding='utf-8') as f:
    for i in range(5):
        f.write(input('عدد: ') + '\n')

total = 0
with open('nums.txt', 'r', encoding='utf-8') as f:
    for line in f:
        total += float(line)
print('جمع:', total)
