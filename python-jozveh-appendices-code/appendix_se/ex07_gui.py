# پیوست ث: مثال ۷: کشیدن یک خانه

import tkinter as tk

win = tk.Tk()
win.title('خانه')
canvas = tk.Canvas(win, width=300, height=260, bg='skyblue')
canvas.pack()
canvas.create_rectangle(0, 200, 300, 260, fill='forestgreen', outline='')
canvas.create_rectangle(80, 110, 220, 200, fill='khaki')
canvas.create_polygon(70, 110, 150, 50, 230, 110, fill='firebrick')
canvas.create_rectangle(135, 150, 165, 200, fill='saddlebrown')
canvas.create_oval(245, 20, 285, 60, fill='gold', outline='')
canvas.create_text(150, 235, text='خانه من', font=('Tahoma', 12))
win.mainloop()
