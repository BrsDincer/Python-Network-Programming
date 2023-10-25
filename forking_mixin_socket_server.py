import os,socket,threading,socketserver

class ForkedClient(object):
  """
  A Client for forking: UNIX
  Use for LINUX

  https://docs.python.org/2/library/socketserver.html
  https://docs.python.org/3/library/socketserver.html
  https://man7.org/linux/man-pages/man2/select.2.html
  """
  def __init__(self,targetIP:str,targetPort:int):
    self.socketEngine = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    self.socketEngine.connect((targetIP,targetPort))
    print(f"CLIENT HAS BEEN CONNECTED TO {targetIP}:{targetPort}")
    self.defaultMessage = "HELLO WORLD - ECHO SERVER"
    self.defaultBufferSize = 2048
  def __str__(self)->str:
    return "Forked Client Process"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return ForkedClient.__doc__
  def RunClient(self):
    currentPID = os.getpid()
    print(f"OPERATION PID: {currentPID}\nSENDING MESSAGE: {self.defaultMessage}")
    sentDataLength = self.socketEngine.send(bytes(self.defaultMessage,"utf-8"))
    print(f"SENT TOTAL {sentDataLength} CHARACTERS")
    response = self.socketEngine.recv(self.defaultBufferSize)
    print(f"RECEIVED FOR OPERATION {currentPID}\n{response[5:]}")
  def ShutDown(self):
    try:
      self.socketEngine.close()
    except:
      pass

class ForkingServerRequestHandler(socketserver.BaseRequestHandler):
  def handle(self):
    data = str(self.request.recv(2048),"utf-8")
    current_process_id = os.getpid()
    response = f"{current_process_id}: {data}"
    print(f"Server sending response: {response}")
    self.request.send(bytes(response,"utf-8"))
    return
  
class ForkingServer(socketserver.ForkingMixIn,socketserver.TCPServer):
  pass

if __name__ == "__main__":
  server = ForkingServer(("localhost",0),ForkingServerRequestHandler)
  ip,port = server.server_address
  serverThread = threading.Thread(target=server.serve_forever)
  serverThread.setDeamon()
  serverThread.start()
  print(f"Server process on PID: {os.getpid()}")
  clientOne = ForkedClient(targetIP=ip,targetPort=port)
  clientOne.RunClient()
  print("First Client is online")
  clientTwo = ForkedClient(targetIP=ip,targetPort=port)
  clientTwo.RunClient()
  print("Second Client is online")
  server.shutdown()
  print("SERVER HAS BEEN CLOSED")
  clientOne.ShutDown()
  print("FIRST CLIENT HAS BEEN CLOSED")
  clientTwo.ShutDown()
  print("SECOND CLIENT HAS BEEN CLOSED")
  try:
    server.socket.close()
    print("SOCKET HAS BEEN CLOSED")
  except:
    pass
