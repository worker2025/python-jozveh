# درس ۱۱: مدیریت خطا، منو و لغزنده
# مثال ۱۳: تنظیم رنگ با سه لغزنده

import tkinter as tk

win = tk.Tk()
win.title('رنگ‌ساز')
win.geometry('300x300')
r = tk.Scale(win, from_=0, to=255, orient='horizontal', label='قرمز')
g = tk.Scale(win, from_=0, to=255, orient='horizontal', label='سبز')
b = tk.Scale(win, from_=0, to=255, orient='horizontal', label='آبی')
for s in (r, g, b):
    s.pack(fill='x', padx=20)
box = tk.Label(win, text='    ', bg='#000000', height=3)
box.pack(fill='x', padx=20, pady=15)

def update(event=None):
    color = f'#{r.get():02x}{g.get():02x}{b.get():02x}'
    box.config(bg=color)

for s in (r, g, b):
    s.config(command=update)
win.mainloop()
