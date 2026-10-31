# پیوست پ: مثال ۶: رمز تصادفی با string و random

import random
import string

chars = string.ascii_letters + string.digits
password = ''.join(random.choice(chars) for _ in range(8))
print(password)
print(len(password))
