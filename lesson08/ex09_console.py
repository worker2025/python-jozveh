# درس ۸: تابع‌ها
# مثال ۹: تابع‌هایی که با هم کار می‌کنند

def is_even(n):
    return n % 2 == 0

def evens_in(nums):
    result = []
    for n in nums:
        if is_even(n):
            result.append(n)
    return result

print(evens_in([1, 2, 3, 4, 5, 6]))
