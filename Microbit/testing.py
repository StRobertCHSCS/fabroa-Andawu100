from microbit import *

pin0.set_analog_period(20)

while True: 
	pin0.write_analog(150)
	sleep(10000)
	pin0.write_analog(100)
	sleep(10000)
	pin0.write_analog(200)
	sleep(10000)