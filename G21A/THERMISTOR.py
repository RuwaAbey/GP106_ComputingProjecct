#Import pyfirmata module.
import pyfirmata
#Import time module.
import time
#Import math module.
import math

#Initial configurations
board = pyfirmata.Arduino('COM3')
alarm_led_pin = board.get_pin('d:11:o') #alarm led
off_button_pin=board.get_pin('d:2:i') #alarm_off push button
Thermister_Pin = board.get_pin('a:1:i') #thermister
buzzer_pin = board.get_pin('d:12:o') #buzzer

# start the utilization service
# this service will handle communication overflows while communicating with the Arduino board via USB intrface .
it = pyfirmata.util.Iterator(board)
it.start()


#Definig Alarm Function 
def alarm():
    #Print the alarm message.
    print('alarm')
    #Execute the loop for buzzer.
    while True:
        buzzer_pin.write(1)                     #turn BUZZER on
        time.sleep(0.5)
        buzzer_pin.write(0)                     #turn BUZZER off
        time.sleep(0.5)
        alarm_led_pin.write(1)                  #turn ALARM LED on
        time.sleep(0.1)
        alarm_led_pin.write(0)                  #turn ALARM LED off
        time.sleep(0.1)
        off_button_val=off_button_pin.read()    #Reading the input of alarm off button.
        time.sleep(0.1)
        #To check whethe the alarm off button is on and verify that the fire is acknowledge.].
        if (off_button_val):
            break
        
#Defining a function to convert the thermistor resistor value to temperature.
def temperature(r):
    R = 871.93                                 #Resistance of thermistore at 302K.
    beta = 2336.042                            #Beta value of the thermistor.
    T2 = 1/((1/302)-(1/beta)*math.log(R/r))    #Equation to calculate the temeperature.
    Tc = T2 - 273.15                           #Converting the temperature value to a celcius value.
    return Tc                                  #Returning the temperature value.


#Executing the while true loop.
while True:
    #Defining variable R1.
    R1 = 10000
    #Defining the variable T_finale.
    T_finale  = 28

    #Defining  the variable i.
    i = 0

    #Read the thermistor analog input.
    thermistor_read = Thermister_Pin.read()
    #Calculating the resistance of the thermistor.
    R2 = R1 *(1 / float(thermistor_read) - 1.0)
    #Using the temeprature function to calculte temperature.
    T_val = temperature(R2)
    #Print the temperature value.
    print(T_val)
    #Print a new line.
    print()
    
    #Detecting a fire using the temperature reading.
    if T_val > 130:
        #Print the fire message.
        print('Fire')
        #Using the alarm function.
        alarm()
        
    #Detecting a increment in temeprature before fire.       
    elif T_val > T_finale:
        i += 1

        #Executing the while loop to detect a continuous increment in  temperature.
        while True:
            if i == 10:
                #Print the message of increment in temperature.
                print('Temperature is Increasing')
                break
            else:
                break
            
    #Continuation of the loop.
    else:
        T_finale = T_val
        continue
        
    T_finale = T_val
