# پیوست ت: مثال ۵: logging

import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
x = 5
logging.debug(f'x = {x}')
logging.info('شروع محاسبه')
logging.warning('مقدار زیاد است')
