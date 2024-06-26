#import modules from Pyfirmatta
from pyfirmata import Arduino, util, INPUT
#IMPORT TIME

#Initial configurations
board = Arduino('COM3')
ldr_pin = 0
board.analog[ldr_pin].mode = INPUT

#start the utilizationn service
#this service will j]handle communication overflows while communicating with the Arduino boeard via USB INTRFACE

it = util.Iterator(board)
it.start()

board.analog[ldr_pin].enable_reporting()

while True:
    print('READ VALUE')
    ldr_val = board.analog[ldr_pin].read()
    print('Analog value:', ldr_val)
    time.sleep(1)
    
