import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('600x250')
root.minsize(width=300, height=150)
root.resizable(True,True)
root.title('Slider')

current_value1 = tk.DoubleVar()
current_value2 = tk.DoubleVar()

def get_current_value1():
    return '{: .0f}'.format(current_value1.get())

def get_current_value2():
    return '{: .0f}'.format(current_value2.get())

value_label1 = ttk.Label(root, text=get_current_value1())
value_label1.place(relx=0.25, rely=.5, anchor="center")

value_label2 = ttk.Label(root, text=get_current_value2())
value_label2.place(relx=0.75, rely=.5, anchor="center")

def slider_changed1(event):
    value_label1.configure(text=get_current_value1())

def slider_changed2(event):
    value_label2.configure(text=get_current_value2())

slider1 = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',
    command=slider_changed1,
    variable=current_value1
)

slider1.place(relx=.25, rely=.375, anchor="center", relwidth=.3)

slider2 = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',
    command=slider_changed2,
    variable=current_value2
)

slider2.place(relx=.75, rely=.375, anchor="center", relwidth=.3)

root.mainloop()


