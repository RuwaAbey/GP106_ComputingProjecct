import time
import math
from pyfirmata import Arduino, util

board = Arduino('COM3')

##defining pins
row1=board.get_pin('d:7:o') #first row in keypad
col1=board.get_pin('d:6:i') #columns in keypad
col2=board.get_pin('d:5:i')
col3=board.get_pin('d:4:i')
col4=board.get_pin('d:3:i')
led_pin = board.get_pin('d:9:o') #led
alarm_led_pin = board.get_pin('d:11:o') #alarm led
button1=board.get_pin('d:8:i') #first push button
button2 = board.get_pin('d:10:i') #second push button
off_button=board.get_pin('d:2:i') #alarm_off push button
buzzer_pin = board.get_pin('d:12:o') #buzzer

iterator = util.Iterator(board)
iterator.start()
pw=[] #getting a list to collect code

##defining the code to enter
def secret_code():
    j=0
    while j<5:
        row1.write(1)
        time.sleep(0.1)
        a=col1.read()
        b=col2.read()
        c=col3.read()
        d=col4.read()

        if a==True:
            j+=1
            pw.append("1")
            print("1")
        elif b==True:
            j+=1
            pw.append("2")
            print("2")
        elif c==True:
            j+=1
            pw.append("3")
            print("3")
        elif d==True:
            j+=1
            pw.append("A")
            print("A")

##defning the alarm and the alarm led
def alarm():
    print('alarm')
    while True:
        buzzer_pin.write(1) #turn BUZZER on
        time.sleep(0.5)
        buzzer_pin.write(0) #turn BUZZER off
        time.sleep(0.5)
        alarm_led_pin.write(1) #turn ALARM LED on
        time.sleep(0.1)
        alarm_led_pin.write(0) #turn ALARM LED off
        time.sleep(0.1)
        off_button_val=off_button.read()
        if (off_button_val):
            break

while True:
    led_pin.write(1) #turn LED on
    time.sleep(0.1)
    led_pin.write(0) #turn LED off
    time.sleep(0.1)

    #reading button2 value, button1 value and off button value
    button2_val = button2.read() 
    button1_val = button1.read()
    off_button_val=off_button.read()

    if button1_val ==1:
        print("Enter your first code : ") #asking for the first code
        start=time.monotonic()
        secret_code() #calling secret_code
        code_1="".join(pw) #joining the list elements
        print(code_1)
        pw=[] #emptying the list 'pw'
        
        #Confidential category secret sequence  = A31A2
        #Secret category secret sequence = 23A1A
        #Top Secret category secret sequence = 31A2A

        ##checking whether the first code is correct according to 3 security clearance categories: confidential, secret and top secret
        if code_1=='A31A2' or code_1=='23A1A' or code_1 == '31A2A': 
            led_pin.write(1) #turning led on
            print("Code 1 is correct")
            print("Enter your second code : ") #asking for the first code
            pw = [] #emptying the list 'pw'
            secret_code() #calling secret_code
            code_2="".join(pw)
            print(code_2)
            
            #Confidential catogary secret sequence  = 33A21
            #Secret catogary secret sequence = A2213
            #Top Secret category secret sequence = 1213A

            ##checking whether both codes are correct according to 3 security clearance categories
            if (code_2=='33A21' and code_1=='A31A2') or (code_2=='A2213' and code_1=='23A1A') or (code_2== '1213A' and code_1 == '31A2A') :
                print("Code 2 is correct")
                time.sleep(3)
                button2_val = button2.read() #readning button2 value 
                pw=[] #emptying the list 'pw'
                if button2_val==True: #checking whether button2 is pressed
                    end=time.monotonic()
                    led_pin.write(1)
                    time_change=end-start
                    print(time_change)
                    if time_change<30: #grant access if time between pressing button1 and button2 is smaller than 30 seconds
                        pw=[]#emptying the list 'pw'
                        print("Access granted")
                           
                    else:
                        #When the time change is exceeded 30 seconds
                        end=time.monotonic()
                        pw=[]#emptying the list 'pw'
                        print('Time limit exceeded')
                        print(end-start)
                        alarm()

                else:
                    #When the second pushbutton didn't press after entering the second code
                    print('Missed second push button')
                    pw=[]#emptying the list 'pw'
                    alarm()

            else:
                #When the code 2 is incorrect
                print("Code 2 is incorrect")
                pw=[]#emptying the list 'pw'
                alarm()

        else:
            #When the code 1 is incorrect
            print("Code 1 is incorrect")
            pw=[]#emptying the list 'pw'
            alarm()

