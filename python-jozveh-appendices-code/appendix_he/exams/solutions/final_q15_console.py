# پیوست ح: آزمون پایان‌ترم - سؤال ۱۵ (نمونه پاسخ)

def stats(nums):
    return len(nums), sum(nums), sum(nums) / len(nums), max(nums)

nums = []
n = int(input('عدد (۰ برای پایان): '))
while n != 0:
    nums.append(n)
    n = int(input('عدد (۰ برای پایان): '))

if nums:
    count, total, avg, biggest = stats(nums)
    print('تعداد:', count)
    print('جمع:', total)
    print('میانگین:', avg)
    print('بزرگ‌ترین:', biggest)
else:
    print('عددی وارد نشد')
