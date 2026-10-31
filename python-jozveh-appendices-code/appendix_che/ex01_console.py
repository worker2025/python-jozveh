# پیوست چ: مثال ۱: کد نامرتب

def f(l,n):
  t=0
  for i in l:
      if i>n: t=t+i
  return t
print(f([1,5,8,2],3))
