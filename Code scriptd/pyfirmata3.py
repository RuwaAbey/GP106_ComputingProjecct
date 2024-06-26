#ir data do -- arduino D 7
#gnd of ir -- arduino gnd
#vcc of ir -- arduino 5v,vin
import pyfirmata
import time
port = 'COM5'
board = pyfirmata.Arduino(port)
pin = 7
#ir_sensor =  board.digital[7].read()
ir = board.get_pin('d:7:i') #d= digital, i=input
it = pyfirmata.util.Iterator(board) #iterator use to stop the buffer overflow
it.start()

while True: #void loop in arduino ide embeded c++
    a = ir.read()#digitalRead(pin)
    print(a)
    time.sleep(0.5)
    
