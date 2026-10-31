# پیوست ث: مثال ۹: توپ پرتابی

import tkinter as tk

win = tk.Tk()
win.title('توپ')
canvas = tk.Canvas(win, width=400, height=300, bg='white')
canvas.pack()
ball = canvas.create_oval(20, 20, 60, 60, fill='tomato')
dx, dy = 4, 3

def move():
    global dx, dy
    canvas.move(ball, dx, dy)
    x1, y1, x2, y2 = canvas.coords(ball)
    if x1 <= 0 or x2 >= 400:
        dx = -dx
    if y1 <= 0 or y2 >= 300:
        dy = -dy
    win.after(20, move)

move()
win.mainloop()
