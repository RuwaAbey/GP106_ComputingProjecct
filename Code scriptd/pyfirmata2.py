import pyfirmata
import time
pin = 13
port = 'COM5'
board = pyfirmata.Arduino(port)
while True:#void loop()
    board.digital[pin].write(1) #digitalWrite(pinnumber,HIGH)
    print('on')
    time.sleep(5)
    
    board.digital[pin].write(0) #digitalWrite(pinnumber,LOW)
    print('off')
    time.sleep(5)

    
