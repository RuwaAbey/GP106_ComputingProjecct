import pyfirmata
import time
import math

board = pyfirmata.Arduino('COM5')

it = pyfirmata.util.Iterator(board)
it.start()

buzzer_pin = board.get_pin('d:7:o')
Thermister_Pin = board.get_pin('a:0:i')
led_pin_1 = board.get_pin('d:8:o')

R1 = 10000
A = 1.1384e-03
B = 2.3245e-04
C = 9.489e-08


while True:
    time.sleep(1)
    thermistor_read = Thermister_Pin.read()
    print(thermistor_read)
    R2 = R1 *(5 / float(thermistor_read) - 1.0)
    T = 1.0 / (A + (B*math.log(R2)) + (C*(pow(math.log(R2),2))))
    Tc = T - 273.15
    print(Tc)

    
   #if Tc >= 135:
       ''' board.digital[led_pin_1].write(1)
        time.sleep(0.2)
        board.digital[led_pin_1].write(0)
        time.sleep(0.2)
        board.digital[buzzer_pin].write(1)
        
    else:
        board.digital[buzzer_pin].write(0)'''

    
  
