import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import ttkbootstrap as tttk

import serial
import time
import serial.tools.list_ports

import time

def sendsValues():
    ports = list(serial.tools.list_ports.comports())
    port = ""
    for p in ports:
        if(p.description.find("Arduino") != -1):
            port = p[0]
            arduino = serial.Serial(port=port, baudrate=9600, timeout=.1)
            def write_read(x):
                arduino.write(bytes(x, 'utf-8'))
                time.sleep(0.05)
                # data = arduino.readline()
                # return data
            contents[1] = get_current_value2()
            contents[0] = get_current_value1()
            print(contents[0] + "\n" + contents[1])
            write_read(contents[0]+contents[1])
            break

    
    # while True:
    #     num = input("Enter a number: ") # Taking input from user
    #     value = write_read(num)
    #     print(value) #  

with open('sens.txt','r') as f:
    contents = f.readlines()
contents[0] = contents[0][:len(contents[0]) - 1]

root = tk.Tk()
style = tttk.Style(theme="superhero")

root.geometry('500x200')
root.minsize(width=300, height=150)
root.maxsize(width=600, height=300)
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



numberFonts = font.Font(family="Helvetica", size=17)

value_label1 = ttk.Label(root, text=get_current_value1())
value_label1.place(relx=0.25, rely=.64, anchor="center")
value_label1['font'] = numberFonts
value_label3 = ttk.Label(root, text="Up")
value_label3.place(relx=0.25, rely=.3, anchor="center")

value_label2 = ttk.Label(root, text=get_current_value2())
value_label2.place(relx=0.75, rely=.64, anchor="center")
value_label2['font'] = numberFonts
value_label4 = ttk.Label(root, text="Down")
value_label4.place(relx=0.75, rely=.3, anchor="center")

myFont = font.Font(family='Helvetica', size=18)
value_label4['font'] = myFont
value_label3['font'] = myFont

value_label5 = ttk.Label(root, text="© FA17 ©")
value_label5.place(relx=0.5, rely=.92, anchor="center")


def slider_changed1(event):
    sendsValues()
    value_label1.configure(text=get_current_value1())
    contents[0] = get_current_value1()
    with open('sens.txt','w') as f:
        f.writelines([contents[0] + "\n", contents[1]])


def slider_changed2(event):
    sendsValues()
    value_label2.configure(text=get_current_value2())
    contents[1] = get_current_value2()
    with open('sens.txt','w') as f:
        f.writelines([contents[0] + "\n", contents[1]])

slider1 = ttk.Scale(
    root,
    from_=1,
    to=9,
    orient='horizontal',
    command=slider_changed1,
    variable=current_value1
)

slider1.place(relx=.25, rely=.48, anchor="center", relwidth=.3)

slider2 = ttk.Scale(
    root,
    from_=1,
    to=9,
    orient='horizontal',
    command=slider_changed2,
    variable=current_value2,
)

slider2.place(relx=.75, rely=.48, anchor="center", relwidth=.3)

root.mainloop()

