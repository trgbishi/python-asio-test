from http.server import BaseHTTPRequestHandler, HTTPServer
'''
用于测试的server
'''
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-Type: application/json','text/html')#Content-Type: application/json
        self.end_headers()
 
        # Send message back to client
        # message = {'op': 'recved'}
        message = {"jsonrpc": 2.0, "method": "sayHello", "params": {"ROOM_ID": 1, "IP": "1.1.1.1", "METRIC": "metric", "TAGS": "tags", "COLL_TIME": "2018-07-26", "COLL_VALUE": 5.5, "alarm_lv": 5},
"id": 1}
        # Write content as utf-8 data
        self.wfile.write(bytes(str(message), "utf8"))
        return
 
def run():
  print('starting server...')
 
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 12345)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
 
 
run()