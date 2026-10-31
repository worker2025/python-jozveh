# درس ۶: حل تمرین ۳: میانگین پنج نمره

total = 0
for i in range(5):
    total += float(input(f'نمره {i + 1}: '))
print('میانگین:', total / 5)
