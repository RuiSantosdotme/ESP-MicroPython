# Complete project details at https://RandomNerdTutorials.com

import machine
from machine import Pin
from time import sleep

led = Pin (2, Pin.OUT)
  
#blink LED
led.value(0)
sleep(1)
led.value(1)
sleep(1)

# wait 5 seconds so that you can catch the ESP awake to establish a serial communication later
# you should remove this sleep line in your final script
sleep(5)
print('Im awake, but Im going to sleep')
sleep(1)

#sleep for indefinite time
machine.deepsleep()