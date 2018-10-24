# Complete project details at https://RandomNerdTutorials.com

from machine import Pin
import time

led = Pin(2, Pin.OUT)

while True:
  led.value(not led.value())
  time.sleep(0.5)
