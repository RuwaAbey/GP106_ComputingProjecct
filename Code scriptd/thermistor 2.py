#import modules from Pyfirmata
import pyfirmata
#import inbuilt time module
import time
import math
board = pyfirmata.Arduino('COM5 (Arduino Uno)')

c = pyfirmata.util.Iterator(board)
c.start()

buzzer_pin = board.get_pin('d:12:o')
Thermister_Pin = board.get_pin('a:0:i')
led_pin_1 = board.get_pin('d:8:o')

R1 = 10000
A = 1.009249522e-03
B = 2.378405444e-04
C = 2.019202697e-07

def temperature(x):
    R2 = R1 * (1023.0 / float(x) - 1.0)
    T = (1.0 / (A + B*math.log(R2) + C*math.log(R2)*math.log(R2)*math.log(R2)))
    Tc = T - 273.15
    return Tc

while True:
    temperature(ThermisterPin)
   
    if Tc >= 47:
        board.digital[led_pin_1].write(1)
        time.sleep(0.2)
        board.digital[led_pin_1].write(0)
        time.sleep(0.2)

        board.digital[buzzer].write(1)
    else:
        board.digital[buzzer].write(0)
