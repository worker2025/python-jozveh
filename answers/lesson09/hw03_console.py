# درس ۹: حل تمرین ۳: تکراری‌ها

nums = [1, 2, 2, 3, 3, 3, 4]
seen = set()
dups = set()
for n in nums:
    if n in seen:
        dups.add(n)
    seen.add(n)
print(dups)
