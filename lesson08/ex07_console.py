# درس ۸: تابع‌ها
# مثال ۷: چند مقدار برگرداندن

def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([4, 9, 2, 7])
print('کمترین:', lo, '- بیشترین:', hi)
