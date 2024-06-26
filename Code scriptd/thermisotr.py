#import modules from Pyfirmata
import pyfirmata
#import inbuilt time module
import time
import math

buzzer = 12
c = pyfirmata.util,Iterator(board)
c.start()


#create an Arduino board instance
board = pyfirmata.Arduino('COM5')

ThermisterPin = 0
Vo = 0
R1 = 10000
R2 = 0
T = 0
Tc = 0
c1 = 1.009249522e-03
c2 = 2.378405444e-04
c3 = 2.019202697e-07

#digital pin numbers
led_pin_1 = 13
board.analog[ThermisterPin].mode = INPUT

while True:
    Vo = analogRead(ThermistorPin)
    R2 = R1 * (1023.0 / float(Vo) - 1.0)
    T = (1.0 / (A + B*math.log(R2) + C*math.(logR2)*math.(logR2)*math.(logR2))
    Tc = T - 273.15
    
    if Tc >= 47:
        board.digital[led_pin_1].write(1)
        time.sleep(0.2)
        board.digital[led_pin_1].write(0)
        time.sleep(0.2)

        board.digital[buzzer].write(1)
    else:
        board.digital[buzzer].write(0)

    

