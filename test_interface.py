import tkinter as tk
from tkinter import ttk
import tkinter.font as font


import time

with open('sens.txt','r') as f:
    contents = f.readlines()
contents[0] = contents[0][:len(contents[0]) - 1]

root = tk.Tk()
root.geometry('500x200')
root.minsize(width=300, height=150)
root.resizable(True,True)
root.title('Pedal Sensitivity Sliders')

current_value1 = tk.DoubleVar()
current_value2 = tk.DoubleVar()

current_value1.set(contents[0])
current_value2.set(contents[1])


def get_current_value1():
    return '{:.0f}'.format(current_value1.get())

def get_current_value2():
    return '{:.0f}'.format(current_value2.get())

value_label1 = ttk.Label(root, text=get_current_value1())
value_label1.place(relx=0.25, rely=.60, anchor="center")
value_label3 = ttk.Label(root, text="Up")
value_label3.place(relx=0.25, rely=.28, anchor="center")

value_label2 = ttk.Label(root, text=get_current_value2())
value_label2.place(relx=0.75, rely=.60, anchor="center")
value_label4 = ttk.Label(root, text="Down")
value_label4.place(relx=0.75, rely=.28, anchor="center")

myFont = font.Font(family='Helvetica', size=15)
value_label4['font'] = myFont
value_label3['font'] = myFont



def slider_changed1(event):
    value_label1.configure(text=get_current_value1())
    contents[0] = get_current_value1()
    with open('sens.txt','w') as f:
        f.writelines([contents[0] + "\n", contents[1]])


def slider_changed2(event):
    value_label2.configure(text=get_current_value2())
    contents[1] = get_current_value2()
    with open('sens.txt','w') as f:
        f.writelines([contents[0] + "\n", contents[1]])

slider1 = ttk.Scale(
    root,
    from_=0,
    to=10,
    orient='horizontal',
    command=slider_changed1,
    variable=current_value1
)

slider1.place(relx=.25, rely=.455, anchor="center", relwidth=.3)

slider2 = ttk.Scale(
    root,
    from_=0,
    to=10,
    orient='horizontal',
    command=slider_changed2,
    variable=current_value2
)

slider2.place(relx=.75, rely=.455, anchor="center", relwidth=.3)

root.mainloop()