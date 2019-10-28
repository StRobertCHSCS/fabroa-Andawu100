from microbit import *
import time

#assign pins
sound = pin0
microservo = pin1
led_blue = pin2
soil_moisture = pin3
crash_sensor = pin4
pir_sensor = pin5

microservo.set_analog_period(20)

while True:
    
    microservo.write_analog(500)
    sleep(2000)


    if pir_sensor.read_digital():
        led_blue.write_digital(1)
       
    else:
         led_blue.write_digital(0)
        
