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

def temeperature(r):
    R = 44591.112
    beta = 135.578
    T2 = 1/((1/303)-(1/beta)*math.log(R/r))
    Tc = T2 - 273.15
    print T2

while True:
    time.sleep(1)
    thermistor_read = Thermister_Pin.read()
    R2 = R1 *(5 / float(thermistor_read) - 1.0)
    temperature(r)
    
    
    
    
