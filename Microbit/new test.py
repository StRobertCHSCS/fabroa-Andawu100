from microbit import *
import music

# assign pins
pir_sensor = pin0
led_red = pin1
sound = pin2


while True:
    # check if motion is detected
    if pir_sensor.read_digital() :
        led_red.write_digital(1)
        music.play(tune, pin=sound)


    else:
        led_red.write_digital(0)

