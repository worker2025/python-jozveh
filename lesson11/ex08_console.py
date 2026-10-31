# درس ۱۱: مدیریت خطا، منو و لغزنده
# مثال ۸: خطای ایجاد شده توسط خودمان (raise)

def set_age(age):
    if age < 0:
        raise ValueError('سن نمی‌تواند منفی باشد')
    return age

try:
    set_age(-5)
except ValueError as e:
    print(e)
