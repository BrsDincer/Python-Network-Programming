import socket,sys

class TCPEchoServer(object):
  def __init__(self):
    self.defaultHost = "localhost"
    self.defaultPort = 9900
    self.defaultUser = 5
    self.defaultPayload = 2048
    self.defaultTimeout = 200
  def __str__(self)->str:
    return "TCP Echo Server"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return TCPEchoServer.__doc__
  def LaunchServer(self):
    socketEngine = socket.socket(socket.AF_INET,
                                 socket.SOCK_STREAM)
    socketEngine.setsockopt(socket.SOL_SOCKET,
                            socket.SO_REUSEADDR,
                            1)
    socketEngine.setblocking(1)
    socketEngine.settimeout(self.defaultTimeout)
    socketEngine.bind((self.defaultHost,self.defaultPort))
    print(f"Server on: {socketEngine.getsockname()}")
    socketEngine.listen(self.defaultUser)
    while True:
      print("Waiting for response from client")
      client,addr = socketEngine.accept()
      data = client.recv(self.defaultPayload)
      if data:
        try:
          print(f"RECEIVED: {data}")
          client.send(data)
          print(f"Echo has been sent to {addr}")
          print("Connection has been closed by server - Mission Done")
          client.close()
        except Exception as err:
          print(f"Connection has been closed by server due to {err}")
          client.close()
      print("Client - OFF")
      client.close()

if __name__ == "__main__":
  TCPEchoServer().LaunchServer()

    