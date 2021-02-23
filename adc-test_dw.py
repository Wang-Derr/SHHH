import serial
import time
import os

# Linux on Seamus' machine
# adc = serial.Serial('/dev/ttyUSB0', 
#                      timeout=1, 
#                      baudrate=115200,
#                      parity=serial.PARITY_NONE,
#                      stopbits=serial.STOPBITS_ONE,
#                      bytesize=serial.EIGHTBITS)

# Win10 on Derrin's machine
adc = serial.Serial('COM5', 
                     timeout=1, 
                     baudrate=115200,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE,
                     bytesize=serial.EIGHTBITS)

if os.path.exists("adc_data.txt"):
    os.remove("adc_data.txt")



n = 0

while(n < 20):
    adc_data = open('adc_data.txt','a+')
    dataIn = adc.read(168)
    dataInAsString = str(dataIn, 'utf-8')

    # Linux on Seamus' machine
    # targetIndex = dataInAsString.index("CH4")

    # Win10 on Derrin's machine
    targetIndex = dataInAsString.index("CH5")

    voltage = dataInAsString[targetIndex + 9:targetIndex + 14]
    adc_data.write(str(n))
    adc_data.write(",")
    adc_data.write(voltage)
    adc_data.write("\n")
    time.sleep(.5)
    n = n + 1
    adc_data.close()
