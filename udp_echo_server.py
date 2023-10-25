import socket

class UDPServer(object):
  def __init__(self):
    self.defaultHost = "localhost"
    self.defaultPort = 9900
    self.defaultPayload = 2048
    self.timeout = 100
    self.defaultUser = 2
  def __str__(self)->str:
    return "UDP Server"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return UDPServer.__doc__
  def LaunchServer(self):
    socketEngine = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    socketEngine.settimeout(self.timeout)
    socketEngine.setblocking(1)
    socketEngine.bind((self.defaultHost,self.defaultPort))
    print(f"Server on: {socketEngine.getsockname()}")
    while True:
      try:
        print("Waiting for connection...")
        data,addr = socketEngine.recvfrom(self.defaultPayload)
        print(f"Message from {addr}:\n{data.decode()}\n Message Length(byte): {len(data)}")
        if data:
          print("Sending echo...")
          sentMessage = socketEngine.sendto(data,addr)
          print(f"Has been sent to {addr}")
        else:
          pass
      except:
        try:
          socketEngine.close()
          break
        except:
          break


if __name__ == "__main__":
  UDPServer().LaunchServer()
