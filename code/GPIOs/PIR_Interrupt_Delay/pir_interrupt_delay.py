# Complete project details at https://RandomNerdTutorials.com

from machine import Pin
from time import sleep

motion = False

def handle_interrupt(v):
  global motion
  motion = True

led = Pin(12, Pin.OUT)
pir = Pin(14, Pin.IN)

pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

while True:
  if motion:
    print('Motion detected!')
    led.value(1)
    sleep(20)
    led.value(0)
    print('Motion stopped!')
    motion = False
