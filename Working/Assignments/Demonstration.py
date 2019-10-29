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

microservo.set_analog_period(5)

while True:
    
#When motion is detected turn on light, if not then turn it off
    if pir_sensor.read_digital():
        led_blue.write_digital(1)
        #music.play(music.BLUES)

    else:
         led_blue.write_digital(0)


while True:

    if ():
        display.scroll("Clear!")
        led_red.write_digital(1)

    else:
         led_red.write_digital(0)
         microservo.write_analog(1000)
         sleep(200)
			



    
        
