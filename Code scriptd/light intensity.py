import pyfirmata
import time
board = pyfirmata.Arduino('COM5')

it = pyfirmata.util.Iterator(board)
it.start()

ldr_pin = board.get_pin('a:0:i') #define LDR pin as Analog Input pin 0
#led_pin = board.get_pin('d:7:o') #define LED pin as Digital Output pin 12
#button_pin = board.get_pin('d:4:i') #define BUTTON pin as Digital Input pin 0
alarm_led_pin = board.get_pin('d:2:o') #define ALARM LED pin as Digital Output pin 7

while True:
    
    '''
    led_pin.write(1) #turn LED on
    time.sleep(0.1)
    led_pin.write(0) #turn LED off
    time.sleep(0.1)
    '''

    light_intensity = ldr_pin.read() #read analog value of data
    #button_val = button_pin.read() #read digital value of button state

    if light_intensity < 300:
        alarm_led_pin.write(1) #turn alarm LED on
        time.sleep(0.05)
    else:
        alarm_led_pin.write(0)

'''data = [str(light_intensity), str(button_val)] #array of data
data = ','.join(data)

client.publish(topic,data) #publish data to MQTT broker using the topic
print('Sent from Arduino ',data)'''
