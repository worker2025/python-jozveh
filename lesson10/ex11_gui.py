# درس ۱۰: کار با فایل
# مثال ۱۱: Text در پنجره: ذخیره و بازکردن

import tkinter as tk

win = tk.Tk()
win.title('یادداشت')
text = tk.Text(win, width=40, height=10)
text.pack(padx=10, pady=10)

def save():
    with open('note.txt', 'w', encoding='utf-8') as f:
        f.write(text.get('1.0', tk.END))

def load():
    with open('note.txt', 'r', encoding='utf-8') as f:
        text.delete('1.0', tk.END)
        text.insert('1.0', f.read())

tk.Button(win, text='ذخیره', command=save).pack(side='left', padx=10)
tk.Button(win, text='باز کردن', command=load).pack(side='left')
win.mainloop()
