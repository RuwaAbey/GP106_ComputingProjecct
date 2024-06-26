#import time module
import time
#import math module
import math
#import pyfirmata module
from pyfirmata import Arduino, util

#initial configurations
board = Arduino('COM3')
p_button = board.get_pin('d:13:i') #push button for pressure
alarm_led_pin = board.get_pin('d:11:o') #alarm led
button2 = board.get_pin('d:10:i') #second push button
off_button=board.get_pin('d:2:i') #alarm_off push button
buzzer_pin = board.get_pin('d:12:o') #buzzer

#start the utilization service
#this service will handle communication overflows while communicating with the Arduino board via USB intrface
iterator = util.Iterator(board)
iterator.start()


##defning the alarm and the alarm led
def alarm():
    #print the alarm message
    print('alarm')
    #execute the loopfor buzzer
    while True:
        buzzer_pin.write(1)    #turn BUZZER on
        time.sleep(0.5)
        buzzer_pin.write(0)    #turn BUZZER off
        time.sleep(0.5)
        alarm_led_pin.write(1) #turn ALARM LED on
        time.sleep(0.1)
        alarm_led_pin.write(0) #turn ALARM LED off
        time.sleep(0.1)
        off_button_val=off_button.read() #reading alarm off button
        if (off_button_val):
            break

##defining pressure alarm
def pressure():
    print("Invalid entry")
    alarm()

sw = p_button.read() #reading push button for pressure
button2_val = button2.read() #reading second push button

if button2_val==True: #checking whether button2 is pressed
    continue
else:
    if sw == 1: # checking whether push button for pressure is pressed
        pressure() #calling pressure definition when the pressure push button is pressed
    
    

        
