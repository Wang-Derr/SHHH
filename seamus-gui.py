from kivy.app import App
from kivy.uix.label import Label
import serial
from kivy.clock import Clock

adc = serial.Serial('/dev/ttyUSB0',
                    timeout=1,
                    baudrate=115200,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS)


class FirstKivy(App):
    def checkSerial(self, argv):
        dataIn = adc.read(168)
        dataInAsString = str(dataIn, 'utf-8')
        targetIndex = dataInAsString.index("CH4")
        refinedString = dataInAsString[targetIndex + 9:targetIndex + 14]
        # voltage = float(refinedString)
        # print(voltage)
        self.MLabel.text = "Voltage " + refinedString + "V"
        print("check")

    def __init__(self):
        App.__init__(self)
        self.adc = serial.Serial('/dev/ttyUSB0',
                                 timeout=1,
                                 baudrate=115200,
                                 parity=serial.PARITY_NONE,
                                 stopbits=serial.STOPBITS_ONE,
                                 bytesize=serial.EIGHTBITS)
        
        self.data = "Has not been updated"
        self.MLabel = Label(text=self.data, font_size='40sp')

        Clock.schedule_interval(self.checkSerial, 1)
        
    def build(self):
        return self.MLabel

if __name__ == '__main__':
    FirstKivy().run()
