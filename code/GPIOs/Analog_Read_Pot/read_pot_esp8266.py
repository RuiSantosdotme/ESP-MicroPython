# Complete project details at https://RandomNerdTutorials.com/micropython-programming-with-esp32-and-esp8266/

from machine import Pin, ADC
from time import sleep

pot = ADC(0)

while True:
  pot_value = pot.read()
  print(pot_value)
  sleep(0.1)
