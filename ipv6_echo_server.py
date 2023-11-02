import socket,sys

class IPV6Server(object):
  """
  socket. AF_UNSPEC. AF_UNSPEC means that getaddrinfo() should return socket addresses for any address family (either IPv4, IPv6, or any other) that can be used.
  The following flags are supported: AI_PASSIVE. Specifies how to fill the returned socket NAME string. If this flag is set, the returned NAME string can be used with the BIND command to bind a socket for accepting new connection requests.
  """
  def __init__(self):
    self.defaultHost = "localhost"
    self.defaultPort = 8600
    self.defaultUserCount = 5
    self.defaultPayload = 4098
  def __str__(self)->str:
    return "IPV-6 Echo Server"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return IPV6Server.__doc__
  def EchoRun(self):
    socketResult = socket.getaddrinfo(self.defaultHost,
                                      self.defaultPort,
                                      socket.AF_UNSPEC,
                                      socket.SOCK_STREAM,
                                      0,
                                      socket.AI_PASSIVE)
    for result in socketResult:
      print(f"\nSERVER SOCKET RESULT:{result}\n")
      a_,socketType,proto_,canon_,server_ = result
      try:
        socketEngine = socket.socket(a_,socketType,proto_)
      except socket.error as serr:
        print(f"SOCKET ERROR: {serr}")
      try:
        socketEngine.bind(server_)
        print(f"RUNNING ON: {socketEngine.getsockname()}")
        socketEngine.listen(self.defaultUserCount)
      except socket.error as serr:
        print(f"CONNECTION ERROR: {serr}")
        try:
          socketEngine.close()
          continue
        except:
          pass
      break
      #sys.exit(1)
    connClient,addrClient = socketEngine.accept()
    print(f"CONNECTION FROM: {addrClient}")
    while True:
      dataFromEcho = connClient.recv(self.defaultPayload)
      print(f"DATA FROM CLIENT: {dataFromEcho.decode()}")
      if not dataFromEcho:
        break
      else:
        pass
      connClient.send(dataFromEcho)
      print("ECHO HAS BEEN SENT")
    connClient.close()
    try:
      socketEngine.close()
    except:
      pass

if __name__ == "__main__":
  IPV6Server().EchoRun()
    

    