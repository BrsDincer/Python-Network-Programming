import socket

class SocketTimeoutControl(object):
  def __init__(self):
    self.newTimeoutValue = 1000
  def __str__(self)->str:
    return "Socket Get/Set Timeout"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return SocketTimeoutControl.__doc__
  def Set(self,socketEngine):
    socketEngine.settimeout(self.newTimeoutValue)
  def Get(self,socketEngine):
    return socketEngine.gettimeout()
  def Control(self):
    socketEngine = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #socket.socket(socket family,socket type)
    defaultTimeout = self.Get(socketEngine)
    print(f"Default Timeout Value: {defaultTimeout}")
    self.Set(socketEngine)
    newTimeout = self.Get(socketEngine)
    print(f"New Timeout Value: {newTimeout}")
    socketEngine.close()

if __name__ == "__main__":
  SocketTimeoutControl().Control()
