# درس ۹: دیکشنری، تاپل و انتخاب‌ها
# مثال ۴: دیکشنری برای شمارش

word = 'banana'
counts = {}
for ch in word:
    counts[ch] = counts.get(ch, 0) + 1
print(counts)
