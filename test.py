import serial
import time
import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
port = ""
for p in ports:
    if(p.description.find("Arduino") != -1):
        port = p[0]
        break

arduino = serial.Serial(port=port, baudrate=9600, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    # data = arduino.readline()
    # return data
while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num)
    print(value) # printing the value