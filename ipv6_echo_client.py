import socket,sys

class IPV6Client(object):
  def __init__(self):
    self.defaultTarget = "localhost"
    self.defaultPort = 8600
    self.defaultPayload = 4098
  def __str__(self)->str:
    return "IPV-6 Client"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return IPV6Client.__doc__
  def EchoRun(self):
    resultClient = socket.getaddrinfo(self.defaultTarget,
                                      self.defaultPort,
                                      socket.AF_UNSPEC,
                                      socket.SOCK_STREAM)
    for result in resultClient:
      print(f"\nCLIENT SOCKET RESULT: {result}\n")
      a_,socketType,proto_,canon,server_ = result
      try:
        socketEngine = socket.socket(a_,socketType,proto_)
        print(f"CLIENT ACTIVE ON: {socketEngine.getsockname()}")
      except socket.error as serr:
        print(f"SOCKET ERROR: {serr}")
      try:
        socketEngine.connect(server_)
        print(f"CONNECTION - DONE: {server_}")
      except socket.error as serr:
        print(f"CONNECTION ERROR: {serr}")
        try:
          socketEngine.close()
          continue
        except:
          pass
    if socketEngine is None:
      print("FAILED - PROCESS")
      sys.exit(1)
    else:
      pass
    message = "ECHO-HELLO MESSAGE"
    socketEngine.send(message.encode("utf-8"))
    while True:
      dataFrom = socketEngine.recv(self.defaultPayload)
      print(f"RECEIVED FROM SERVER: {dataFrom}")
      if not dataFrom:
        break
    try:
      socketEngine.close()
    except:
      pass
  

if __name__ == "__main__":
  IPV6Client().EchoRun()