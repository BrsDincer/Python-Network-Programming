import sys
from http.server import BaseHTTPRequestHandler,HTTPServer

class HTTPBase(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header("Content-type","text/html")
    self.end_headers()
    self.wfile.write("HELLO WORLD".encode())
    return
  
class CustomHTTPServer(HTTPServer):
  def __init__(self,host,port):
    server_address = (host,port)
    HTTPServer.__init__(self,server_address=server_address,RequestHandlerClass=HTTPBase)

class RunServer(object):
  def __init__(self):
    self.defaultHost = "127.0.0.1"
    self.defaultPort = 8800
  def __str__(self)->str:
    return "Server Base"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return RunServer.__doc__
  def Launch(self):
    try:
      server = CustomHTTPServer(self.defaultHost,self.defaultPort)
      print(f"SERVER ON: {self.defaultHost}:{self.defaultPort}")
      server.serve_forever()
    except Exception as err:
      print(f"SERVER ERROR: {err}")
    except KeyboardInterrupt:
      print("SERVER HAS BEEN CLOSED BY USER")
      server.socket.close()

if __name__ == "__main__":
  RunServer().Launch()