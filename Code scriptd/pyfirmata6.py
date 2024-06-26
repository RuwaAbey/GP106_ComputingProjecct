import pyfirmata
import time

board = pyfirmata.Arduino (" COM5 ")
it = pyfirmata.util.Iterator(board)
it.start()


buzzer_pin = 13
def temperature(x):
    R2 = R1 * (1023.0 / float(x) - 1.0)
    T = (1.0 / (A + B*math.log(R2) + C*math.log(R2)*math.log(R2)*math.log(R2)))
    Tc = T - 273.15
    print(Tc)
    return Tc
board.digital[led_pin_1].mode = pyfirmata.OUTPUT
board.digital[led_pin_1].mode = pyfirmata.OUTPUT
board.analog[ThermisterPin].mode = pyfirmata.INPUT
while True:
    thermistor_output = board.analog[ThermisterPin].read() 
    temperature(thermistor_output)
   
    if Tc >= 47:
        board.digital[led_pin_1].write(1)
        time.sleep(0.2)
        board.digital[led_pin_1].write(0)
        time.sleep(0.2)

        board.digital[buzzer_pin = 13].write(1)
