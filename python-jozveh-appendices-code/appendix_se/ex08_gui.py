# پیوست ث: مثال ۸: رسم با کلیک ماوس

import tkinter as tk

win = tk.Tk()
win.title('کلیک کن')
canvas = tk.Canvas(win, width=400, height=300, bg='white')
canvas.pack()

def draw(event):
    r = 15
    canvas.create_oval(event.x - r, event.y - r, event.x + r, event.y + r,
                       fill='skyblue')

canvas.bind('<Button-1>', draw)
win.mainloop()
