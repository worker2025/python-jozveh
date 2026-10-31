# درس ۷: لیست‌ها
# مثال ۹: ساخت لیست با ورودی کاربر

nums = []
for i in range(3):
    nums.append(int(input('عدد: ')))
print(nums)
print('جمع:', sum(nums))
