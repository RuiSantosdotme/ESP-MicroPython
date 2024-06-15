# Complete project details at https://RandomNerdTutorials.com/micropython-programming-with-esp32-and-esp8266/

from machine import Pin, Timer
from time import sleep

# LED pin
led_pin = 13
led = Pin(led_pin, Pin.OUT)

# Callback function for the timer
def toggle_led(timer):
    led.value(not led.value())  # Toggle the LED state (ON/OFF)

# Create a periodic timer
blink_timer = Timer(1)
blink_timer.init(mode=Timer.PERIODIC, period=500, callback=toggle_led)  # Timer repeats every half second

try:
    # Main loop (optional)
    while True:
        print('Main Loop is running')
        sleep(2)
except KeyboardInterrupt:
    # Keyboard interrupt occurred, deinitialize the timer
    blink_timer.deinit()
    print('Timer deinitialized')
    # Turn off the LED
    led_pin.value(0)
