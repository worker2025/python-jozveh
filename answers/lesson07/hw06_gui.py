# درس ۷: حل تمرین ۶: انتقال بین دو لیست

import tkinter as tk

win = tk.Tk()
win.geometry('420x300')
left = tk.Listbox(win, width=16, exportselection=False)
right = tk.Listbox(win, width=16, exportselection=False)
left.pack(side='left', padx=15, pady=15)
right.pack(side='right', padx=15, pady=15)
for name in ['علی', 'سارا', 'رضا', 'مریم']:
    left.insert(tk.END, name)

def move_right():
    sel = left.curselection()
    if sel:
        right.insert(tk.END, left.get(sel[0]))
        left.delete(sel[0])

def move_left():
    sel = right.curselection()
    if sel:
        left.insert(tk.END, right.get(sel[0]))
        right.delete(sel[0])

tk.Button(win, text='>>', command=move_right).pack(pady=40)
tk.Button(win, text='<<', command=move_left).pack()
win.mainloop()
