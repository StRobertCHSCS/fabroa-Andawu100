from microbit import *

microservo = pin8

microservo.set_analog_period(10)

while True: 
			microservo.write_analog(500)
			sleep(2000)