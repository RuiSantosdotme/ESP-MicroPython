# Complete project details at https://RandomNerdTutorials.com/micropython-programming-with-esp32-and-esp8266/

from machine import Pin
from time import sleep

led = Pin(5, Pin.OUT)
button = Pin(4, Pin.IN)

while True:
  led.value(button.value())
  sleep(0.1)
