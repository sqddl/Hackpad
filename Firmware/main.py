import board
import digitalio
from kmk import KMKKeyboard
from kmk.keys import KC
from kmk.modules import Layer


keyboard = KMKKeyboard()


switch_pins = [board.D0, board.D2, board.D1, board.D3,
               board.D7, board.D8, board.D9, board.D10]

for pin in switch_pins:
    switch = digitalio.DigitalInOut(pin)
    switch.switch_to_input(pull=digitalio.Pull.UP)

keyboard.pins = {
    board.D5: KC.A,  
    board.D2: KC.B,  
    board.D7: KC.C,  
    board.D8: KC.D,  
    board.D9: KC.E,  
    board.D10: KC.F, 
    board.D0: KC.G,  
    board.D1: KC.H   


}


if __name__ == "__main__":
    while True:

        keyboard.poll()
