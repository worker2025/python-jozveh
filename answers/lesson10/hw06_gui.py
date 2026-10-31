# درس ۱۰: حل تمرین ۶: دفترچه خاطرات

import tkinter as tk
from datetime import date

win = tk.Tk()
win.title('خاطرات')
text = tk.Text(win, width=40, height=8)
text.pack(padx=10, pady=10)

def record():
    with open('diary.txt', 'a', encoding='utf-8') as f:
        f.write(f'{date.today()}: {text.get("1.0", tk.END).strip()}\n')
    text.delete('1.0', tk.END)

tk.Button(win, text='ثبت', command=record).pack(pady=5)
win.mainloop()
