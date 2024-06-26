#ir sensor data pin which is do-- digital pin of arduino 7
#gnd - gnd
#vcc - vin, 5v
#buzzer big terminal 5v
#buzzer small terminal -- digital pin of arduino 12
import pyfirmata
import time
port = 'COM5'
board = pyfirmata.Arduino(port)
ir = board.get_pin('d:7:i')
buzzer = 12
c = pyfirmata.util.Itterator(board)
c.start()

while True:
    value = ir.read()
    print(value)
    if value is False:
        board.digital[buzzer].write(0)
    elif value is True:
        board.digital[buzzer].write(1)
    
                                
