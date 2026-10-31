# پیوست ت: مثال ۳: برنامه‌ای برای قدم‌زدن

def total_price(prices, tax):
    total = 0
    for p in prices:
        total += p
    return total * (1 + tax)

items = [100, 250, 75]
result = total_price(items, 0.25)
print(result)
