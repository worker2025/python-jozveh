# درس ۸: تابع‌ها
# مثال ۵: آرگومان با نام

def intro(name, city='تهران', age=15):
    print(f'{name} اهل {city} و {age} ساله است')

intro('علی')
intro('سارا', 'شیراز')
intro('رضا', age=20)
intro(age=12, name='مریم', city='اصفهان')
