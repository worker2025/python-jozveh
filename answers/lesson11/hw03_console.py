# درس ۱۱: حل تمرین ۳: safe_int

def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None

print(safe_int('25'))
print(safe_int('abc'))
