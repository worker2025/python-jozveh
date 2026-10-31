# پیوست پ: حل تمرین ۳

import random
import string

password = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
print(password)
