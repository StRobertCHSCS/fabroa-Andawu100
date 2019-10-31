from microbit import *
import time 
import music

#assign pins
sound = pin0
microservo = pin8
led_blue = pin2
soil_moisture = pin3
crash_sensor = pin4
pir_sensor = pin5
led_red = pin6


while True:
    
#When motion is detected turn on light
    if pir_sensor.read_digital():
        led_blue.write_digital(1)
        #amusic.play(music.BLUES)

    else:
         led_blue.write_digital(0)


while True:

    if temperature == (20):
        display.scroll("Clear")
        led_red.write_digital(0)

    elif temperature => (20):
        led_red.write_digital(1)
    
    else:
         display.scroll("Something is not right")
         


			



    
        
