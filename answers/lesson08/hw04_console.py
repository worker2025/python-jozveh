# درس ۸: حل تمرین ۴: شمارش حروف صدادار

def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in 'aeiou':
            count += 1
    return count

print(count_vowels('Hello World'))
