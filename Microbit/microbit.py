from microbit import *
import music

# pins
ADKeypad_pin = pin2
Buzzer_pin = pin0

while True:
    # buttonA
    if ADKeypad_pin.read_analog() > 0 and ADKeypad_pin.read_analog() < 10:
        music.play('d4:4', pin=Buzzer_pin)

    # buttonB
    if ADKeypad_pin.read_analog() > 45 and ADKeypad_pin.read_analog() < 55:
        music.play('e4:4', pin=Buzzer_pin)

    # button c
    if ADKeypad_pin.read_analog() > 90 and ADKeypad_pin.read_analog() < 100:
        music.play('f4:4', pin=Buzzer_pin)

    # button d
    if ADKeypad_pin.readanalog() > 136 and ADKeypad_pin.read_analog() < 139
        music.play('g4:4', pin=Buzzer_pin)

    # button e
    if ADKeypad_pin.readanalog() > 535 and ADKeypad_pin.read_analog() < 545
        music.play('g4:4', pin=Buzzer_pin)
 

