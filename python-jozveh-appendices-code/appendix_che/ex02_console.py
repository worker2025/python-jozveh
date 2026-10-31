# پیوست چ: مثال ۲: همان کد با رعایت PEP 8

def sum_above(numbers, limit):
    """مجموع عددهای بزرگ‌تر از limit را برمی‌گرداند."""
    total = 0
    for n in numbers:
        if n > limit:
            total += n
    return total


print(sum_above([1, 5, 8, 2], 3))
