import pyfirmata
import time
pin = 13
port = 'COM5'
board = pyfirmata.Arduino(port)
board.digital[pin].write(1) #digitalWrite(pinnumber,HIGH)
time.sleep(5)
print('on')
board.digital[pin].write(0) #digitalWrite(pinnumber,LOW)
time.sleep(5)
print('off')
