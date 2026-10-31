# درس ۷: حل تمرین ۱: زوج‌ها

evens = []
for i in range(1, 21):
    if i % 2 == 0:
        evens.append(i)
print(evens)
print('جمع:', sum(evens))
