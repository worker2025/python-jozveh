# درس ۹: حل تمرین ۱: شمارش کلمه

text = input('یک متن: ')
counts = {}
for w in text.split():
    counts[w] = counts.get(w, 0) + 1
for w, c in counts.items():
    print(w, ':', c)
