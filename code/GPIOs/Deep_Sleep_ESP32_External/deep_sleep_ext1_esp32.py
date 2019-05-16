# Complete project details at https://RandomNerdTutorials.com

import machine
import esp32
from machine import Pin
from time import sleep

wake1 = Pin(14, mode = Pin.IN)
wake2 = Pin(12, mode = Pin.IN)

#level parameter can be: esp32.WAKEUP_ANY_HIGH or esp32.WAKEUP_ALL_LOW
esp32.wake_on_ext1(pins = (wake1, wake2), level = esp32.WAKEUP_ANY_HIGH)

#your main code goes here to perform a task

print('Im awake. Going to sleep in 10 seconds')
sleep(10)
print('Going to sleep now')
machine.deepsleep()
