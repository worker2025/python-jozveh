# درس ۶: حل تمرین ۶: اعداد اول

import tkinter as tk

win = tk.Tk()
win.geometry('200x320')
lb = tk.Listbox(win, width=15, height=15)
lb.pack(padx=20, pady=20)

for n in range(2, 50):
    is_prime = True
    for d in range(2, n):
        if n % d == 0:
            is_prime = False
            break
    if is_prime:
        lb.insert(tk.END, n)

win.mainloop()
