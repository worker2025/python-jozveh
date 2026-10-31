# درس ۱۰: کار با فایل
# مثال ۸: خواندن عددها و محاسبه

total = 0
count = 0
with open('scores.txt', 'r', encoding='utf-8') as f:
    for line in f:
        total += int(line)
        count += 1
print('میانگین:', total / count)
