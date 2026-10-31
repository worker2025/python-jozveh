# درس ۶: حلقه‌ها
# مثال ۱۰: منوی تکراری

while True:
    cmd = input('سلام یا خروج؟ ')
    if cmd == 'سلام':
        print('سلام به شما!')
    elif cmd == 'خروج':
        print('خداحافظ')
        break
    else:
        print('دستور نامعتبر')
