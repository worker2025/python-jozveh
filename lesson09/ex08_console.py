# درس ۹: دیکشنری، تاپل و انتخاب‌ها
# مثال ۸: دفترچه تلفن متنی

book = {}
while True:
    cmd = input('add / find / quit: ')
    if cmd == 'add':
        name = input('نام: ')
        book[name] = input('شماره: ')
    elif cmd == 'find':
        name = input('نام: ')
        print(book.get(name, 'پیدا نشد'))
    elif cmd == 'quit':
        break
