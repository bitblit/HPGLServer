import serial
ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)
x = ser.read()          # read one byte
s = ser.read(10)        # read up to ten bytes (timeout)
line = ser.readline()   # read a '\n' terminated line
ser.close()