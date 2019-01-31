# Complete project details at https://RandomNerdTutorials.com

def read_sensor():
  global temp, temp_percentage, hum
  temp = temp_percentage = hum = 0
  try:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    if (isinstance(temp, float) and isinstance(hum, float)) or (isinstance(temp, int) and isinstance(hum, int)):
      msg = (b'{0:3.1f},{1:3.1f}'.format(temp, hum))

      temp_percentage = (temp+6)/(40+6)*(100)
      # uncomment for Fahrenheit
      #temp = temp * (9/5) + 32.0
      #temp_percentage = (temp-21)/(104-21)*(100)

      hum = round(hum, 2)
      return(msg)
    else:
      return('Invalid sensor readings.')
  except OSError as e:
    return('Failed to read sensor.')

def web_page():
  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1">
  <style>body{padding: 20px; margin: auto; width: 50%; text-align: center;}
  .progress{background-color: #F5F5F5;} .progress.vertical{position: relative;
  width: 25%; height: 60%; display: inline-block; margin: 20px;}
  .progress.vertical > .progress-bar{width: 100% !important;position: absolute;bottom: 0;}
  .progress-bar{background: linear-gradient(to top, #f5af19 0%, #f12711 100%);}
  .progress-bar-hum{background: linear-gradient(to top, #9CECFB 0%, #65C7F7 50%, #0052D4 100%);}
  p{position: absolute; font-size: 1.5rem; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 5;}</style></head>
  <body><h1>DHT Sensor</h1><div class="progress vertical">
  <p>"""+str(temp)+"""*<p>
  <div role="progressbar" style="height: """+str(temp_percentage)+"""%;" class="progress-bar"></div></div><div class="progress vertical">
  <p>"""+str(hum)+"""%</p>
  <div role="progressbar" style="height: """+str(hum)+"""%;" class="progress-bar progress-bar-hum"></div></div></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  print('Content = %s' % str(request))
  sensor_readings = read_sensor()
  print(sensor_readings)
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
