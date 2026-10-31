# پیوست ث: حل تمرین ۳

import tkinter as tk

win = tk.Tk()
win.title('آدم‌برفی')
c = tk.Canvas(win, width=240, height=340, bg='lightblue')
c.pack()
c.create_oval(50, 220, 190, 330, fill='white')
c.create_oval(70, 130, 170, 230, fill='white')
c.create_oval(90, 60, 150, 130, fill='white')
c.create_oval(105, 80, 115, 90, fill='black')
c.create_oval(125, 80, 135, 90, fill='black')
c.create_polygon(120, 92, 120, 100, 150, 96, fill='orange')
c.create_rectangle(90, 40, 150, 62, fill='black')
c.create_rectangle(105, 15, 135, 42, fill='black')
win.mainloop()
