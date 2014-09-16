import serial

with open('knownGood.hpgl', 'r') as f:
    hp = f.read()
f.closed

print 'Before'
print hp
print 'After'

#ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1, xonxoff=False, rtscts=True, writeTimeout=2, dsrdtr=True, interCharTimeout=2)
#ser = serial.Serial(ort=None, baudrate=9600, bytesize=EIGHTBITS, parity=PARITY_NONE, stopbits=STOPBITS_ONE, timeout=None, xonxoff=False, rtscts=False, writeTimeout=None, dsrdtr=False, interCharTimeout=None)
#ser = serial.Serial(0)  # open first serial port
print ser.name          # check which port was really used
ser.write(hp)
#x = ser.read()          # read one byte
#s = ser.read(10)        # read up to ten bytes (timeout)
line = ser.readline()   # read a '\n' terminated line
ser.close()