import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import ttkbootstrap as tttk

import serial
import time
import serial.tools.list_ports

import time
normalOrder = True

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
            switch = switchDirection()
            keyboard = KeyBoardMode()
            keyboardModeSensitivity = get_current_value3()

            print(contents[0] + "\n" + contents[1]+"\n"+str(keyboard)+"\n"+str(keyboardModeSensitivity))
            write_read(str(switch)+contents[0]+contents[1]+str(keyboard)+str(keyboardModeSensitivity))
            break

with open('sens.txt','r') as f:
    contents = f.readlines()
contents[0] = contents[0][:len(contents[0]) - 1]

root = tk.Tk()
style = tttk.Style(theme="superhero")

root.geometry('500x300')
root.minsize(width=300, height=150)
root.maxsize(width=600, height=300)
root.resizable(True,True)
root.title('Pedal Sensitivity Sliders')

current_value1 = tk.DoubleVar()
current_value2 = tk.DoubleVar()
current_value3 = tk.DoubleVar()

current_value1.set(contents[0])
current_value2.set(contents[1])


def get_current_value1():
    return '{:.0f}'.format(current_value1.get())

def get_current_value2():
    return '{:.0f}'.format(current_value2.get())

def get_current_value3():
    return '{:.0f}'.format(current_value3.get())



numberFonts = font.Font(family="Helvetica", size=17)

value_label1 = ttk.Label(root, text=get_current_value1())
value_label1.place(relx=0.225, rely=.433, anchor="center")
value_label1['font'] = numberFonts
value_label3 = ttk.Label(root, text="Up")
value_label3.place(relx=0.225, rely=.233, anchor="center")

value_label2 = ttk.Label(root, text=get_current_value2())
value_label2.place(relx=0.775, rely=.433, anchor="center")
value_label2['font'] = numberFonts
value_label4 = ttk.Label(root, text="Down")
value_label4.place(relx=0.775, rely=.233, anchor="center")

myFont = font.Font(family='Helvetica', size=18)
value_label4['font'] = myFont
value_label3['font'] = myFont

value_label5 = ttk.Label(root, text="© FA17 ©")
value_label5.place(relx=0.5, rely=.92, anchor="center")

value_label6 = ttk.Label(root, text=get_current_value3())
value_label6.place(relx=.225, rely=.766, anchor="center")
value_label7 = ttk.Label(root, text="Clicking Mode")
value_label7.place(relx=0.775, rely=.766, anchor="center")
value_label6['font'] = myFont
value_label7['font'] = font.Font(family='Helvetica', size=10)



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

def slider_changed3(event):
    sendsValues()
    value_label6.configure(text=get_current_value3())
    
        
slider1 = ttk.Scale(
    root,
    from_=1,
    to=9,
    orient='horizontal',
    command=slider_changed1,
    variable=current_value1
)

slider1.place(relx=.225, rely=.333, anchor="center", relwidth=.3)

slider2 = ttk.Scale(
    root,
    from_=1,
    to=9,
    orient='horizontal',
    command=slider_changed2,
    variable=current_value2,
)

slider2.place(relx=.775, rely=.333, anchor="center", relwidth=.3)

slider3 = ttk.Scale(
    root,
    from_=1,
    to=5,
    orient='horizontal',
    command=slider_changed3,
    variable=current_value3,
)

slider3.place(relx=.225, rely=.666, anchor="center", relwidth=.3)

def Simpletoggle():
    
    if toggle_button.config('text')[-1] == 'ON':
        toggle_button.config(text='OFF')
    else:
        toggle_button.config(text='ON')
    sendsValues()
def KeyBoardMode():
    if toggle_button.config('text')[-1] == 'ON':
        return 1
    else:
        return 0
toggle_button = ttk.Button(
    root,
    text="OFF",
    width=10,
    command=Simpletoggle,
)
def switchDirection():
    if toggle_button2.config('text')[-1] == 'Switch Pedals':
        return 1
    else:
        return 0
def Simpletoggle2():
    if toggle_button2.config('text')[-1] == 'Switch Pedals':
        toggle_button2.config(text=' Switch-Pedals ')
    else:
        toggle_button2.config(text='Switch Pedals')
    sendsValues()

toggle_button2 = ttk.Button(
    root,
    text="Switch Pedals",
    width=10,
    command=Simpletoggle2,
)
toggle_button2.place(relx=.5, rely=.333, anchor="center", relwidth=.2)

toggle_button.place(relx=.775, rely=.666, anchor="center", relwidth=.3)

root.mainloop()

