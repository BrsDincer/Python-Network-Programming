import socket

class MultiPlexWebServer(object):
  """
  Socket Server - Using EPOLL
  Test for UNIX (LINUX)

  socket. fileno() Return the socket's file descriptor (a small integer), or -1 on failure.
  
  """
  def __init__(self):
    self.defaultHost = "localhost"
    self.defaultPort = 0
    self.defaultUserCount = 5
    self.serverTemplate = (
      b"HTTP/1.0 200 OK\r\n"
      b"Content-Type: text/plain\r\n\r\n"
      b"HELLO WORLD!"
    )
    self.defaultPayload = 2048
    print(f"\n\nSERVER TEMPLATE:\n\n{self.serverTemplate}\n\n")
  def __str__(self)->str:
    return "Multi-Plex Web Server Base"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return MultiPlexWebServer.__doc__
  def RunServer(self):
    try:
      socketEngine = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      socketEngine.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
      socketEngine.bind((self.defaultHost,self.defaultPort))
      socketEngine.listen(self.defaultUserCount)
      print("LISTENING")
      socketEngine.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
      print(f"SERVER ON: {socketEngine.getsockname()}")
      while True:
        connection,addr = socketEngine.accept()
        print(f"\nCONNECTION FROM: {addr}\n")
        recvFromOne = connection.recv(self.defaultPayload)
        print(f"\nFIRST RECEIVED:\n{recvFromOne.decode()}")
        connection.sendall(self.serverTemplate)
    except Exception as err:
      print(f"SERVER ERROR: {str(err)}")
      try:
        socketEngine.close()
      except:
        pass
      try:
        connection.close()
      except:
        pass

if __name__ == "__main__":
  MultiPlexWebServer().RunServer()
            

