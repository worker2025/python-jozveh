# درس ۷: لیست‌ها
# مثال ۴: حذف عضو

colors = ['قرمز', 'آبی', 'سبز', 'زرد']
colors.remove('آبی')
print(colors)
last = colors.pop()
print(last, colors)
del colors[0]
print(colors)
