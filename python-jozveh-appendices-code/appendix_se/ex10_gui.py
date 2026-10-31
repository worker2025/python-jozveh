# پیوست ث: مثال ۱۰: حرکت با کلیدهای جهت‌نما

import tkinter as tk

win = tk.Tk()
win.title('حرکت')
canvas = tk.Canvas(win, width=400, height=300, bg='white')
canvas.pack()
box = canvas.create_rectangle(180, 130, 220, 170, fill='purple')

def key(event):
    step = 10
    if event.keysym == 'Left':
        canvas.move(box, -step, 0)
    elif event.keysym == 'Right':
        canvas.move(box, step, 0)
    elif event.keysym == 'Up':
        canvas.move(box, 0, -step)
    elif event.keysym == 'Down':
        canvas.move(box, 0, step)

win.bind('<Key>', key)
win.mainloop()
