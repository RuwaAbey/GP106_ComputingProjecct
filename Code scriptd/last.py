import pyfirmata
import time
import serial


board = pyfirmata.Arduino('COM5')

it = pyfirmata.util.Iterator(board)
it.start()

push_button_1 = board.get_pin('d:7:i')
push_button_2 = board.get_pin('d:8:i')
led_pin_1 = board.get_pin('d:6:o')
buzzer_pin = board.get_pin('d:5:o')

connected = False
ser = serial.Serial('COM5',9600)
print(ser.name)

while not connected:
    serin = ser.read()
    connected = True

while True:
    initial = time.monotonic()
    push_button_1_reading = push_button_1.read()
    if push_button_1_reading is True:
        print('Please enter the code')
        var = ser.read()
        print(var)
        if var == 'AAA' or var == 'BBB' or var === 'CCC':
            print('Code is correct')
            var = ser.read()
            print(var)
            if var = 'AAADASH' or var == 'BBBDASH' or var == 'CCCDASH':
                print('Code is correct')
                
        else:
            print('Ivalid Entry')
            board.digital[led_pin_1].write(1)
            board.digital[buzzer_pin].write(1)
            
            
            
        
    
    
    
