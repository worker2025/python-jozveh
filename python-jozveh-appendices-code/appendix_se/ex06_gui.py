# پیوست ث: مثال ۶: ماشین‌حساب

import tkinter as tk

win = tk.Tk()
win.title('ماشین‌حساب')
win.resizable(False, False)
display = tk.Entry(win, justify='right', font=('Tahoma', 18), width=14)
display.grid(row=0, column=0, columnspan=4, padx=6, pady=6)
display.insert(0, '0')
state = {'a': None, 'op': None, 'new': True}

def press(ch):
    if state['new']:
        display.delete(0, tk.END)
        state['new'] = False
    display.insert(tk.END, ch)

def set_op(op):
    try:
        state['a'] = float(display.get())
    except ValueError:
        return
    state['op'] = op
    state['new'] = True

def equals():
    if state['op'] is None:
        return
    try:
        b = float(display.get())
    except ValueError:
        return
    a, op = state['a'], state['op']
    try:
        if op == '+':
            r = a + b
        elif op == '-':
            r = a - b
        elif op == '*':
            r = a * b
        else:
            r = a / b
    except ZeroDivisionError:
        r = 'خطا'
    display.delete(0, tk.END)
    display.insert(0, r)
    state['op'] = None
    state['new'] = True

def clear():
    display.delete(0, tk.END)
    display.insert(0, '0')
    state.update(a=None, op=None, new=True)

keys = [['7', '8', '9', '/'], ['4', '5', '6', '*'],
        ['1', '2', '3', '-'], ['0', '.', '=', '+']]
for r, row in enumerate(keys, start=1):
    for c, ch in enumerate(row):
        if ch in '+-*/':
            cmd = lambda o=ch: set_op(o)
        elif ch == '=':
            cmd = equals
        else:
            cmd = lambda x=ch: press(x)
        tk.Button(win, text=ch, width=4, height=2, command=cmd).grid(
            row=r, column=c, padx=2, pady=2)
tk.Button(win, text='C', command=clear).grid(
    row=5, column=0, columnspan=4, sticky='ew', padx=2, pady=4)
win.mainloop()
