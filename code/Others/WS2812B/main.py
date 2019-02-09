# Complete project details at https://RandomNerdTutorials.com

import machine, neopixel
import time

# number of pixels
n = 14
# strip control gpio
p = 14

np = neopixel.NeoPixel(machine.Pin(p), n)

# set single pixel (1st pixel = index [0]) to red color
np[0] = (255, 0, 0)
np.write()
time.sleep(1)

# set strip color
def set_color(r, g, b):
  for i in range(n):
    np[i] = (r, g, b)
    np.write()

set_color(0, 0, 255)
time.sleep(1)

# fade in/out
def fade_in_out(color, wait):
  for i in range(0, 4 * 256, 8):
    for j in range(n):
      if (i // 256) % 2 == 0:
        val = i & 0xff
      else:
        val = 255 - (i & 0xff)
        if color == 'red':
          np[j] = (val, 0, 0)
        elif color == 'green':
          np[j] = (0, val, 0)
        elif color == 'blue':
          np[j] = (0, 0, val)
        elif color == 'purple':
          np[j] = (val, 0, val)
        elif color == 'yellow':
          np[j] = (val, val, 0)
        elif color == 'teal':
          np[j] = (0, val, val)
        elif color == 'white':
          np[j] = (val, val, val)
      np.write()
    time.sleep_ms(wait)

#fade_in_out('red', 0)
fade_in_out('green', 10)
#fade_in_out('blue', 25)
#fade_in_out('purple', 10)
fade_in_out('yellow', 10)
fade_in_out('teal', 10)
#fade_in_out('white', 10)
time.sleep(1)

# bounce
def bounce(r, g, b, wait):
  for i in range(4 * n):
    for j in range(n):
      np[j] = (r, g, b)
    if (i // n) % 2 == 0:
      np[i % n] = (0, 0, 0)
    else:
      np[n - 1 - (i % n)] = (0, 0, 0)
    np.write()
    time.sleep_ms(wait)
      
bounce(255, 0, 125, 50)
time.sleep(1)

# cycle
def cycle(r, g, b, wait):
  for i in range(4 * n):
    for j in range(n):
      np[j] = (0, 0, 0)
    np[i % n] = (r, g, b)
    np.write()
    time.sleep_ms(wait)

cycle(0, 255, 0, 50)
time.sleep(1)

# function to go through all colors 
def wheel(pos):
  # Input a value 0 to 255 to get a color value.
  # The colours are a transition r - g - b - back to r.
  if pos < 0 or pos > 255:
    return (0, 0, 0)
  if pos < 85:
    return (255 - pos * 3, pos * 3, 0)
  if pos < 170:
    pos -= 85
    return (0, 255 - pos * 3, pos * 3)
  pos -= 170
  return (pos * 3, 0, 255 - pos * 3)

# rainbow 
def rainbow_cycle(wait):
  for j in range(255):
    for i in range(n):
      rc_index = (i * 256 // n) + j
      np[i] = wheel(rc_index & 255)
    np.write()
    time.sleep_ms(wait)

rainbow_cycle(10)
rainbow_cycle(5)
time.sleep(1)

# turn off all pixels
def clear():
  for i in range(n):
    np[i] = (0, 0, 0)
    np.write()

clear()
