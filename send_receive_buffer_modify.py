import socket

class ModifyBufferSize(object):
  """
  SOL_SOCKET(int): Use this constant as the level argument to getsockopt or setsockopt to manipulate the socket-level options
  SOL_TCP: protocol
  TCP_NODELAY and TCP_CORK basically control packet “Nagling,” or automatic concatenation of small packets into bigger frames performed by a Nagle algorithm. 

  https://www.techrepublic.com/article/tcp-ip-options-for-high-performance-data-transmission/
  https://www.cems.uwe.ac.uk/~irjohnso/linsock/Book%20Notes/Appendices/Data%20Tables/TCP-Level%20Socket%20Options.html
  """
  def __init__(self):
    self.bufferSizeSend = 4096
    self.bufferSizeReceive = 4096
  def __str__(self)->str:
    return "Modify Buffer Size"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return ModifyBufferSize.__doc__
  def Modify(self,socketEngine):
    buffSizeSend = socketEngine.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
    buffSizeReceive = socketEngine.getsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF)
    print(f"Default Buffer Size-SEND: {buffSizeSend}")
    print(f"Default Buffer Size-RECEIVE: {buffSizeReceive}")
    socketEngine.setsockopt(socket.SOL_TCP,socket.TCP_NODELAY,1)
    socketEngine.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,self.bufferSizeSend)
    socketEngine.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,self.bufferSizeReceive)
    newSizeSend = socketEngine.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
    newSizeReceive = socketEngine.getsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF)
    print(f"New Buffer Size-SEND: {newSizeSend}")
    print(f"New Buffer Size-RECEIVE: {newSizeReceive}")
    socketEngine.close()
  def Run(self):
    socketEngine = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    self.Modify(socketEngine)

if __name__ == "__main__":
  ModifyBufferSize().Run()
