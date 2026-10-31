# ایده ۸: دوز (راهنمای ساخت)

import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title('دوز')
turn = {'p': 'X'}
buttons = []

def check():
    b = [x['text'] for x in buttons]
    lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
             (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for a, c, d in lines:
        if b[a] != '' and b[a] == b[c] == b[d]:
            return b[a]
    return None

def click(i):
    if buttons[i]['text'] != '':
        return
    buttons[i].config(text=turn['p'])
    winner = check()
    if winner:
        messagebox.showinfo('پایان', f'برنده: {winner}')
        win.destroy()
        return
    turn['p'] = 'O' if turn['p'] == 'X' else 'X'

for i in range(9):
    b = tk.Button(win, text='', width=6, height=3, font=('Tahoma', 16),
                  command=lambda i=i: click(i))
    b.grid(row=i // 3, column=i % 3)
    buttons.append(b)
win.mainloop()
