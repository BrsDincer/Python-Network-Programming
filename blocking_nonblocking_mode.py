import socket

class BlockingSetup(object):
  """
  By default, TCP sockets are placed in a blocking mode.
  This means the control is not returned to your program until some specific operation is complete.

  On many occasions, you don't want to keep your program waiting forever, either for a response
  from the server or for any error to stop the operation. For example, when you write a web
  browser client that connects to a web server, you should consider a stop functionality that
  can cancel the connection process in the middle of this operation. This can be achieved by placing the socket in the non-blocking mode.

  setblocking(1) to set up blocking or setblocking(0) to unset blocking


  """
  def __init__(self):
    self.ipClass = socket.AF_INET
    self.protocolClass = socket.SOCK_STREAM
  def __str__(self)->str:
    return "Blocking Setup"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return BlockingSetup.__doc__
  def CreateSocketEngine(self):
    socketEngine = socket.socket(self.ipClass,self.protocolClass)
    return socketEngine
  def ChangeMode(self):
    socketEngine = self.CreateSocketEngine()
    socketEngine.setblocking(1)
    socketEngine.settimeout(0.5)
    socketEngine.bind(("127.0.0.1",0))
    socketAddress = socketEngine.getsockname()
    print(f"Server On: {socketAddress}")
    try:
      while (1):
        socketEngine.listen(1)
      socketEngine.close()
    except:
      try:
        socketEngine.close()
      except:
        pass

if __name__ == "__main__":
  BlockingSetup().ChangeMode()
    


