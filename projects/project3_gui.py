# پروژه ۳: آزمون چندگزینه‌ای

import tkinter as tk
from tkinter import messagebox

questions = [
    {'q': 'خروجی print(2 ** 3) چیست؟', 'opts': ['6', '8', '9'], 'ans': 1},
    {'q': 'کدام نوع داده برای متن است؟', 'opts': ['int', 'str', 'bool'], 'ans': 1},
    {'q': 'نماد کامنت در پایتون کدام است؟', 'opts': ['//', '#', '--'], 'ans': 1},
]
state = {'i': 0, 'score': 0}

win = tk.Tk()
win.title('آزمون پایتون')
win.geometry('360x300')
q_label = tk.Label(win, font=('Tahoma', 13), wraplength=320)
q_label.pack(pady=15)
choice = tk.IntVar(value=-1)
radios = []
for k in range(3):
    r = tk.Radiobutton(win, variable=choice, value=k)
    r.pack(anchor='w', padx=40)
    radios.append(r)

def show():
    q = questions[state['i']]
    q_label.config(text=q['q'])
    choice.set(-1)
    for k, r in enumerate(radios):
        r.config(text=q['opts'][k])

def next_q():
    if choice.get() == -1:
        messagebox.showwarning('توجه', 'یک گزینه انتخاب کنید')
        return
    if choice.get() == questions[state['i']]['ans']:
        state['score'] += 1
    state['i'] += 1
    if state['i'] == len(questions):
        messagebox.showinfo('پایان',
                            f'امتیاز شما: {state["score"]} از {len(questions)}')
        win.destroy()
    else:
        show()

tk.Button(win, text='بعدی', command=next_q).pack(pady=20)
show()
win.mainloop()
