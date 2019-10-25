from microbit import *

microservo = pin1

microservo.set_analog_period(5)

while True: 
			microservo.write_analog(500)
			sleep(2000)