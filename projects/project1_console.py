# پروژه ۱: دفترچه کارها (نسخه متنی)

FILE = 'tasks.txt'

def load():
    try:
        with open(FILE, 'r', encoding='utf-8') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

def save(tasks):
    with open(FILE, 'w', encoding='utf-8') as f:
        for t in tasks:
            f.write(t + '\n')

tasks = load()
while True:
    cmd = input('add / list / done / quit: ')
    if cmd == 'add':
        tasks.append(input('کار: '))
        save(tasks)
    elif cmd == 'list':
        for i, t in enumerate(tasks, 1):
            print(i, t)
    elif cmd == 'done':
        try:
            n = int(input('شماره کار: '))
            print('انجام شد:', tasks.pop(n - 1))
            save(tasks)
        except (ValueError, IndexError):
            print('شماره نامعتبر')
    elif cmd == 'quit':
        break
