#Import time module
import time
from pyfirmata import Arduino, util

board = Arduino('COM3')

##defining pins
led_pin = board.get_pin('d:9:o') #define led as Digital output pin 9
alarm_led_pin = board.get_pin('d:11:o') #define alarm led as Digital output pin 11
button2 = board.get_pin('d:10:i') #define second push button as Digital input pin 10
ldr_pin = board.get_pin('a:0:i') #define ldr as Analog input pin 0 
buzzer_pin = board.get_pin('d:12:o') #define buzzer as Digital output pin 12

iterator = util.Iterator(board)
iterator.start()

cycles = 0 #getting number of times when ldr darkens

##defining the alarm and the alarm led
def alarm():
    print('alarm')
    while True: #execute the loop for buzzer
        buzzer_pin.write(1) #turn buzzer on
        time.sleep(0.5)
        buzzer_pin.write(0) #turn buzzer off
        time.sleep(0.5)
        alarm_led_pin.write(1) #turn alarm led on
        time.sleep(0.1)
        alarm_led_pin.write(0) #turn alarm led off
        time.sleep(0.1)
        off_button_val=off_button.read() #reading off button value
        if (off_button_val): #if off_button is pressed(indicating guards came and looked into the alarm) break the buzzer loop 
            break

while True:
    led_pin.write(1) #turn led on
    time.sleep(0.1)
    led_pin.write(0) #turn led off
    time.sleep(0.1)

    #reading button2 value and ldr value
    button2_val = button2.read()
    ldr_val = ldr_pin.read()
    
    if(button2_val): #checking whether button2 is pressed
        while cycles < 3: #getting ldr values until ldr darkens for two times
            ldr_val = ldr_pin.read()
            time.sleep(1)
            led_pin.write(1)
            print("LDR Val %s" % ldr_val) #printing ldr value
            fire_alarm() #calling fire_alarm function
            time.sleep(1)
            
            if ldr_val2 > 0.7: #counting cycles when ldr darkens
                cycles+=1
                print(cycles) #printing number of cycles
                fire_alarm() #calling fire_alarm
                led_pin.write(0) #turning led off
                time.sleep(3) #letting ldr to be dark for 3 seconds

            if cycles==3: #firing alarm if ldr darkens for three times
                alarm_led_pin.write(1)
                alarm()
                time.sleep(0.5)
                cycles=0 #taking number of cycles as zero for the next loop
                print('alarmed')
                fire_alarm()
                break

            else:
                continue

    elif ldr_val > 0.7: #firing alarm if ldr darkens when button2 is not pressed
        alarm_led_pin.write(1)
        fire_alarm() #calling fire_alarm function
        alarm()
        print('Unusual activity')
        time.sleep(1)

    else:
        continue
