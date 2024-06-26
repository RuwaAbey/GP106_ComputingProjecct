#Group 21-A
#02/03/2022

#Import time and math modules
import time
import math
from pyfirmata import Arduino, util

board = Arduino('COM5')

##defining pins
row1=board.get_pin('d:7:o') #define first row in keypad as Digital output pin 7
col1=board.get_pin('d:6:i') #define columns in keypad as Digital input pins 6,5,4 and 3
col2=board.get_pin('d:5:i')
col3=board.get_pin('d:4:i')
col4=board.get_pin('d:3:i')
button1=board.get_pin('d:8:i') #define first push button as Digital input pin 8
button2 = board.get_pin('d:10:i') #define second push button as Digital input pin 10
off_button=board.get_pin('d:2:i') #define alarm_off push button as Digital input pin 2
p_button = board.get_pin('d:13:i') #define push button for pressure as Digital input pin 13
led_pin = board.get_pin('d:9:o') #define led as Digital output pin 9
alarm_led_pin = board.get_pin('d:11:o') #define alarm led as Digital output pin 11
buzzer_pin = board.get_pin('d:12:o') #define buzzer as Digital output pin 12
ldr_pin = board.get_pin('a:0:i') #define ldr as Analog input pin 0
Thermister_Pin = board.get_pin('a:1:i') #define thermister as Analog input pin 1

iterator = util.Iterator(board)
iterator.start()

R1 = 10000 #value of the resistor which is connected to the thermistor
cycles = 0 #getting number of times when ldr darkens
pw=[] #getting a list to collect code

##defining the code function to enter
def secret_code():
    j=0
    while j<5: #taking the code of five digits
        row1.write(1) 
        time.sleep(0.1)
        a=col1.read()
        b=col2.read()
        c=col3.read()
        d=col4.read()

        if a==True: #printing '1' if col1 is pressed in row1
            j+=1
            pw.append("1") #appending '1' to the list 'pw'
            print("1")
        elif b==True: #printing '2' if col2 is pressed in row1
            j+=1
            pw.append("2") #appending '2' to the list 'pw'
            print("2")
        elif c==True: #printing '3' if col3 is pressed in row1
            j+=1
            pw.append("3") #appending '3' to the list 'pw'
            print("3")
        elif d==True: #printing 'A' if col4 is pressed in row1
            j+=1
            pw.append("A") #appending 'A' to the list 'pw'
            print("A")

##defining the alarm and the alarm led function
def alarm():
    print('alarm')
    #execute the loop for buzzer
    while True:
        buzzer_pin.write(1) #turn buzzer on
        time.sleep(0.5)
        buzzer_pin.write(0) #turn buzzer off
        time.sleep(0.5)
        alarm_led_pin.write(1) #turn alarm led on
        time.sleep(0.1)
        alarm_led_pin.write(0) #turn alarm led off
        time.sleep(0.1)
        off_button_val=off_button.read() #reading off button value
        if (off_button_val): #if off_button is pressed(indicating guards came and looked into the alarm), break the buzzer loop
            break

##defining pressure alarm function
def pressure():
    print("Invalid entry")
    alarm()

##defining temperature function to convert the resistor value of the thermistor to temperature
def temperature(r):
    R = 871.93
    beta = 2336.042
    T2 = 1/((1/302)-(1/beta)*math.log(R/r))
    Tc = T2 - 273.15
    return Tc

##defining fire alarm and temperature increasing alert
def fire_alarm():
    i = 0 #defining number of times the temperature is increasing
    T_finale  = 28 #defining the variable T_finale as 28 celsius(room temperature)
    thermistor_read = Thermister_Pin.read() #reading thermistor value
    R2 = R1 *(1 / float(thermistor_read) - 1.0) #calculating the resistance of the thermistor
    T_val = temperature(R2) #calling the temperature function to calculate temperature
    print('Temperature value is ',T_val)
    print()

    if T_val > 130: #detecting a fire using the temperature reading when temperature reading is more than 130
        print('Fire')
        alarm() #calling alarm function

    elif T_val > T_finale: #detecting fire increment for 10 temperature readings
        i += 1
        while True:
            if i == 10: #giving temperature increasing alert 
                print('Temperature is Increasing')
                T_finale = T_val
                break
            else:
                break

#executing the while True loop
while True:
    led_pin.write(1) #turn led on
    time.sleep(0.1)
    led_pin.write(0) #turn led off
    time.sleep(0.1)

    #reading push button value, button2 value, button1 value, ldr value and off button value
    sw = p_button.read() 
    button2_val = button2.read() 
    button1_val = button1.read()
    ldr_val = ldr_pin.read()
    off_button_val=off_button.read()

    fire_alarm() #calling fire_alarm 

    if button1_val ==1:
        print("Enter your first code : ") #asking for the first code
        start=time.monotonic()
        secret_code() #calling secret_code
        code_1="".join(pw) #joining the elements in the list 
        print(code_1)
        pw=[] #emptying the list 'pw'
        
        #Confidential category secret sequence  = A31A2
        #Secret category secret sequence = 23A1A
        #Top Secret sequence = 31A2A

        ##checking whether the first code is correct according to 3 security clearance categories: confidential, secret, and top secret
        if code_1=='A31A2' or code_1=='23A1A' or code_1 == '31A2A': 
            led_pin.write(1) #turning led on
            print("Your first code is correct.")
            print("Enter your second code : ") #asking for the first code
            pw = [] #emptying the list 'pw'
            secret_code() #calling secret_code
            code_2="".join(pw)
            print(code_2)
            
            #Confidential category secret sequence  = 33A21
            #Secret category secret sequence = A2213
            #Top Secret sequence = 1213A

            ##checking whether both codes are correct according to 3 security clearance categories
            if (code_2=='33A21' and code_1=='A31A2') or (code_2=='A2213' and code_1=='23A1A') or (code_2== '1213A' and code_1 == '31A2A') : 
                time.sleep(3)
                button2_val = button2.read() #readning button2 value 
                pw=[] #emptying the list 'pw'
                if button2_val==True: #checking whether button2 is pressed
                    end=time.monotonic()
                    led_pin.write(1)
                    time_change=end-start
                    print(time_change)
                    pw=[]
                    if time_change<30: #granting access if time difference between pressing button1 and button2 is smaller than 30 seconds
                        pw=[]
                        print("Access granted")
                        fire_alarm()

                        while cycles < 3: #getting ldr values until ldr darkens for two times
                            off_button_val=off_button.read()
                            ldr_val = ldr_pin.read()
                            time.sleep(1)
                            led_pin.write(1)
                            print("LDR Val %s" % ldr_val)
                            fire_alarm()
                            
                            if ldr_val > 0.7: #counting cycles when ldr darkens
                                cycles+=1
                                print(cycles)
                                fire_alarm()
                                led_pin.write(0)
                                time.sleep(8) #letting ldr to be dark for 8 seconds

                            if cycles==3: #firing alarm if ldr darkens for three times
                                alarm_led_pin.write(1)
                                alarm()
                                time.sleep(0.5)
                                cycles=0 #taking number of cycles as zero for the next loop
                                print('alarmed')
                                fire_alarm()
                                break

                            if off_button_val==1: #checking whether the off_button is pressed to check whether the guards have left
                                pw=[]
                                cycles=0
                                break #break the loop, if off_button is pressed
                            
                            else:
                                continue
                            
                        if off_button_val==1: #continue the loop from the beginning, if off_button is pressed when guards are leaving 
                            pw=[]
                            continue
                            
                    elif sw == 1: #calling pressure function if pressure button is pressed when the time difference between pressing button1 and button2 is larger than 30 seconds
                        pressure()
                    else: #calling alarm function if pressure button is pressed when the time difference between pressing button1 and button2 is larger than 30 seconds
                        print("Time change exceeded.")
                        alarm()
                        
                elif sw == 1: #calling pressure function if pressure button is pressed when button2 is not pressed
                    pressure()
                else: #calling alarm function if pressure button is pressed when button2 is not pressed
                    end=time.monotonic()
                    print(end-start)
                    pw=[]
                    alarm()
                    
            elif sw == 1: #calling pressure function if pressure button is pressed when the second code is incorrect
                pressure()
            else: #calling alarm function if pressure button is pressed when the second code is incorrect
                pw=[]
                print("Your second code is incorrect.")
                alarm()
                
        elif sw == 1: #calling pressure function if pressure button is pressed when the first code is incorrect
            pressure()
        else: #calling alarm function if pressure button is pressed when the first code is incorrect
            print("Your first code is incorrect.")
            alarm()

    elif ldr_val > 0.7: #firing alarm if ldr darkens when button1 is not pressed
        alarm_led_pin.write(1)
        fire_alarm()
        print('Unusual activity')
        alarm()
        time.sleep(1)
    
    elif sw == 1: #calling pressure function if pressure button is pressed when button1 is not pressed
        pressure()

    else: #continue the loop
        continue
        
    time.sleep(0.1)
