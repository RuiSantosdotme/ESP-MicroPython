# Complete project details at https://RandomNerdTutorials.com

def web_page():
  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
  <body><h1>Hello, World!</h1></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  print('Content = %s' % str(request))
  response = web_page()
  conn.send('HTTP/1.1 200 OK')
  conn.send('Content-Type: text/html; encoding=utf8\nContent-Length: ')
  conn.send(str(len(response)))
  conn.send('\nConnection: close\n')
  conn.send('\n')
  conn.send(response)
  conn.close()
