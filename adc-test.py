import serial

adc = serial.Serial('/dev/ttyUSB0', 
                     timeout=1, 
                     baudrate=115200,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE,
                     bytesize=serial.EIGHTBITS)

dataIn = adc.read(168)
dataInAsString = str(dataIn, 'utf-8')
targetIndex = dataInAsString.index("CH4")
refinedString = dataInAsString[targetIndex + 9:targetIndex + 14]
voltage = float(refinedString)
print(voltage)

