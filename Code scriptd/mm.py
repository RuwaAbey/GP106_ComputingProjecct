import pyfirmata
import time

board = pyfirmata.Arduino('COM5')

it = pyfirmata.util.Iterator(board)
it.start()


Thermister_Pin = board.get_pin('a:0:i')

R1 = 10000

while True:
    time.sleep(1)
    thermistor_read = Thermister_Pin.read()
    print(thermistor_read)
    R2 = R1 *(1 / float(thermistor_read) - 1.0)
    print(R2)
    

