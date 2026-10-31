# درس ۵: تصمیم‌گیری با if
# مثال ۷: سال کبیسه (شرط تو در تو)

year = int(input('سال: '))
if year % 400 == 0:
    print('کبیسه')
elif year % 100 == 0:
    print('غیر کبیسه')
elif year % 4 == 0:
    print('کبیسه')
else:
    print('غیر کبیسه')
