import serial

f = open('knownGood.hpgl', 'r')
print f

with open('workfile', 'r') as f:
     hp = f.read()
f.closed

print 'Before'
print hp
print 'After'

ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)
x = ser.read()          # read one byte
s = ser.read(10)        # read up to ten bytes (timeout)
line = ser.readline()   # read a '\n' terminated line
ser.close()