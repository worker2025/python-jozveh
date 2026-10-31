# درس ۸: حل تمرین ۶: فیبوناچی

import tkinter as tk

def fib(n):
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

win = tk.Tk()
win.geometry('200x320')
lb = tk.Listbox(win, width=15, height=15)
lb.pack(padx=20, pady=20)
for x in fib(12):
    lb.insert(tk.END, x)
win.mainloop()
