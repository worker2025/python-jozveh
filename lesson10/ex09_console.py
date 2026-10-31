# درس ۱۰: کار با فایل
# مثال ۹: بررسی وجود فایل

import os

if os.path.exists('names.txt'):
    print('فایل هست')
else:
    print('فایل پیدا نشد')
