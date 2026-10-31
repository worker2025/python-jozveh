# درس ۷: حل تمرین ۲: مرتب‌سازی تا ۰

nums = []
n = int(input('عدد (۰ برای پایان): '))
while n != 0:
    nums.append(n)
    n = int(input('عدد (۰ برای پایان): '))
nums.sort()
print(nums)
