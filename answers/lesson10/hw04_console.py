# درس ۱۰: حل تمرین ۴: شمارش کلمه در فایل

word = input('کلمه: ')
with open('diary.txt', 'r', encoding='utf-8') as f:
    text = f.read()
print(word, 'تعداد:', text.count(word))
