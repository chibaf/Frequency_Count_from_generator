import serial, sys
import binascii

ser=serial.Serial(sys.argv[1],sys.argv[2])
print("connected to: " + ser.portstr)
while True:
  line = ser.readline()
  line1=line.strip().decode('utf-8')
  print(line1)
ser.close()
