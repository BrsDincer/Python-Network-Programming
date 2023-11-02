import socket,select

class MultiPlexWebServer(object):
  """
  Socket Server - Using EPOLL
  Test for UNIX (LINUX)

  socket. fileno() Return the socket's file descriptor (a small integer), or -1 on failure.
  
  """
  def __init__(self):
    self.defaultHost = "localhost"
    self.defaultPort = 0
    self.defaultUserCount = 1
    self.serverTemplate = (
      b"HTTP/1.1 200 OK\r\n"
      b"Date: Mon, 1 Apr 2013 01:01:01 GMT\r\n"
      b"Content-Type: text/plain\r\n"
      b"Content-Length: 25\r\n\r\n"
      b"HELLO WORLD!"
    )
    self.defaultPayload = 2048
    self.eolList = [b"\n\r",b"\n\r\n"]
    self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    self.socket.bind((self.defaultHost,self.defaultPort))
    self.socket.listen(self.defaultUserCount)
    self.socket.setblocking(0)
    self.socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
    print("EPOLL SERVER HAS BEEN STARTED")
    print(f"SERVER ON: {self.socket.getsockname()}")
    self.epoll = select.epoll()
    self.epoll.register(self.socket.fileno(),select.EPOLLIN)
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
      connections = {}; requests = {}; responses = {}
      while True:
        events = self.epoll.poll(1)
        for fNo,event in events:
          if fNo == self.socket.fileno():
            connection,addr = self.socket.accept()
            connection.setblocking(0)
            self.epoll.register(connection.fileno(),select.EPOLLIN)
            connections[connection.fileno()] = connection
            requests[connection.fileno()] = b""
            responses[connection.fileno()] = self.serverTemplate
          elif event & select.EPOLLIN:
            requests[fNo] += connections[fNo].recv(self.defaultPayload)
            if self.eolList[0] in requests[fNo] or self.eollist[1] in requests[fNo]:
              self.epoll.modify(fNo,self.EPOLLOUT)
              print("-"*40+"\n"+requests[fNo].decode()[:-2])
            else:
              pass
          elif event & select.EPOLLOUT:
            bytesOutWritten = connections[fNo].send(responses[fNo])
            responses[fNo] = responses[fNo][bytesOutWritten]
            if len(responses[fNo]) == 0:
              self.epoll.modify(fNo,0)
              connections[fNo].shutdown(socket.SHUT_RDWR)
            else:
              pass
          elif event & select.EPOLLHUP:
            self.epoll.unregister(fNo)
            connections[fNo].close()
            del connections[fNo]
    finally:
      self.epoll.unregister(self.socket.fileno())
      self.epoll.close()
      self.socket.close()

if __name__ == "__main__":
  MultiPlexWebServer().RunServer()
            

