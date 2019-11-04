from microbit import *
import time 
import music

#assign pins
crash_sensor = pin0
pir_sensor = pin1
soil_moisture = pin2
sound = pin10
led_blue = pin8
led_red = pin16

while True:
    
#When motion is detected turn on light
    if pir_sensor.read_digital():
        led_blue.write_digital(1)
        music.play(music.BLUES)

    else:
         led_blue.write_digital(0)


while True:

    if crash_senser.was_pressed():
       led_red.write_digital(0)

    else:
         led_red.write_digital(1)
         display.scroll("Something is not right")
