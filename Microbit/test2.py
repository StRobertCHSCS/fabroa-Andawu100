from microbit import *

while True:
buf = bytearray(1)
buf[0]=0
i2c.write(0x24, buf, repeat=True)
sleep(1000)
buf[0]=1
i2c.write(0x24, buf, repeat=True)
sleep(1000)