# درس ۷: لیست‌ها
# مثال ۱۰: انتخاب تصادفی

import random

names = ['علی', 'سارا', 'رضا', 'مریم']
print(random.choice(names))
random.shuffle(names)
print(names)
print(random.randint(1, 6))
