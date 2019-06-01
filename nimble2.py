import serial
arduino = serial.Serial('COM10',9600, timeout=.1)
while True:
	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
	if data:
		print(data)
