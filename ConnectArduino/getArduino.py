import serial
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)



try:
    while 1:
        response = ser.readline()
        
        print 'signal'
        print response
except KeyboardInterrupt:
    ser.close()
