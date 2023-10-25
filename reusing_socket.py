import socket

class ReuseSocketOperation(object):
  """
  You may run this script from one console window and try to connect to this server from
  another console window by typing telnet localhost 8282.

  How to make Telnet enable on Windows:
  https://phoenixnap.com/kb/telnet-windows
  """
  def __init__(self):
    self.localPort = 8282
  def __str__(self)->str:
    return "Reusing Socket"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return ReuseSocketOperation.__doc__
  def CheckAndModifyReusing(self):
    socketEngine = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socketEngine.setblocking(0)
    socketEngine.settimeout(5)
    oldStateReuse = socketEngine.getsockopt(socket.SOL_SOCKET,
                                            socket.SO_REUSEADDR)
    print(f"Old Socket State: {oldStateReuse}")
    socketEngine.setsockopt(socket.SOL_SOCKET,
                            socket.SO_REUSEADDR,
                            1)
    newStateReuse = socketEngine.getsockopt(socket.SOL_SOCKET,
                                            socket.SO_REUSEADDR)
    print(f"New Socket State: {newStateReuse}")
    #newStateReuse.close()
    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serverSocket.setblocking(0)
    serverSocket.settimeout(10)
    serverSocket.setsockopt(socket.SOL_SOCKET,
                            socket.SO_REUSEADDR,
                            1)
    serverSocket.bind(("",self.localPort))
    serverSocket.listen(1)
    serverSocketName = serverSocket.getsockname()
    print(f"Server On: {serverSocketName}")
    while True:
      try:
        conn,addr = serverSocket.accept()
        print(f"New Connection by: {addr[0]}:{addr[1]}")
      except KeyboardInterrupt:
        #serverSocketName.close()
        break
      except socket.error as msg:
        print(f"Error: {msg}")

if __name__ == "__main__":
  ReuseSocketOperation().CheckAndModifyReusing()

