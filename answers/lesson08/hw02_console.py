# درس ۸: حل تمرین ۲: میانگین

def average(nums):
    return sum(nums) / len(nums)

grades = []
for i in range(3):
    grades.append(float(input('نمره: ')))
print('میانگین:', average(grades))
