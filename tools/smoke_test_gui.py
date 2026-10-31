import sys, runpy, traceback, tkinter as tk
from tkinter import messagebox, filedialog
for n in ('showinfo','showwarning','showerror','askquestion','askyesno'):
    setattr(messagebox, n, lambda *a, **k: None)
filedialog.asksaveasfilename = lambda *a, **k: ''
filedialog.askopenfilename = lambda *a, **k: ''
errors = []
def walk(w):
    yield w
    for c in w.winfo_children():
        yield from walk(c)
def fake_mainloop(self, n=0):
    try:
        ws = list(walk(self))
        for w in ws:
            if isinstance(w, tk.Entry):
                w.delete(0, tk.END); w.insert(0, '3')
            elif isinstance(w, tk.Text):
                w.insert('1.0', 'متن آزمایشی')
            elif isinstance(w, tk.Listbox) and w.size() == 0:
                w.insert(tk.END, 'a'); w.insert(tk.END, 'b')
        for w in ws:
            if isinstance(w, tk.Listbox) and w.size() > 0:
                w.selection_set(0)
        for w in ws:
            if isinstance(w, tk.Button):
                try:
                    w.invoke()
                except tk.TclError as e:
                    if 'invalid command' in str(e) or 'bad window' in str(e): break
                    errors.append(('TclError', str(e)))
                except Exception as e:
                    errors.append((type(e).__name__, str(e)))
        for w in ws:
            try:
                if isinstance(w, tk.Scale): w.set(5)
            except tk.TclError: pass
    except Exception as e:
        errors.append(('harness', repr(e)))
tk.Misc.mainloop = fake_mainloop
tk.Tk.mainloop = fake_mainloop
try:
    runpy.run_path(sys.argv[1], run_name='__main__')
except SystemExit:
    pass
except Exception as e:
    errors.append(('load', type(e).__name__ + ': ' + str(e)))
for t, m in errors:
    print(t, m)
