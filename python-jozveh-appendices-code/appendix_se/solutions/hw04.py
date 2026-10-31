# پیوست ث: حل تمرین ۴

import tkinter as tk

win = tk.Tk()
canvas = tk.Canvas(win, width=400, height=300, bg='white')
canvas.pack()
speed = tk.Scale(win, from_=1, to=15, orient='horizontal', label='سرعت')
speed.set(4)
speed.pack(fill='x')
ball = canvas.create_oval(20, 20, 60, 60, fill='tomato')
dirs = {'x': 1, 'y': 1}

def move():
    s = speed.get()
    canvas.move(ball, dirs['x'] * s, dirs['y'] * s)
    x1, y1, x2, y2 = canvas.coords(ball)
    if x1 <= 0 or x2 >= 400:
        dirs['x'] = -dirs['x']
    if y1 <= 0 or y2 >= 300:
        dirs['y'] = -dirs['y']
    win.after(20, move)

move()
win.mainloop()
