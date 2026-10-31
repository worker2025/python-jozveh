# پیوست ت: مثال ۴: assert

def average(nums):
    assert len(nums) > 0, 'لیست خالی است'
    return sum(nums) / len(nums)

print(average([1, 2, 3]))
try:
    print(average([]))
except AssertionError as e:
    print('خطا:', e)
