# درس ۱۱: مدیریت خطا، منو و لغزنده
# مثال ۷: گرفتن همه خطاها و نمایش پیام

try:
    nums = [1, 2, 3]
    print(nums[10])
except Exception as e:
    print('خطا رخ داد:', e)
