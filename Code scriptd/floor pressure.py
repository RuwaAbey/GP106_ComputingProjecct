import pyfirmata
import time

board = pyfirmata.Arduino()

it = pyfirmata.util.Iterator(board)
it.start()

p_button = board.get_pin('d:10:i')
led_pin_1 = board.get_pin('d:8:o')
buzzer_pin = board.get_pin('d:12:o')

while True:
    aw = p_button2.read()
    sw = p_button.read()
    if aw is True:
        led_pin_1.write(0)
        buzzer_pin.write(0)
    else:
        if sw is True:
            led_pin_1.write(1)
            buzzer_pin.write(1)
        else:
            led_pin_1.write(0)
            buzzer_pin.write(0)
