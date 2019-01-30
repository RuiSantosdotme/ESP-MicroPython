# Complete project details at https://RandomNerdTutorials.com

from machine import TouchPad, Pin
from time import sleep

touch_pin = TouchPad(Pin(4))

while True:
  touch_value = touch_pin.read()
  print(touch_value)
  sleep(0.5)