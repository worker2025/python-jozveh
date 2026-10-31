# درس ۸: حل تمرین ۱: تابع اول بودن

def is_prime(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(10))
