import socket

class UDPClient(object):
  def __init__(self):
    self.defaultTarget = "localhost"
    self.defaultPort = 9900
    self.defaultPayload = 2048
  def __str__(self)->str:
    return "UDP Client"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return UDPClient.__doc__
  def LaunchClient(self):
    socketEngine = socket.socket(socket.AF_INET,
                                 socket.SOCK_DGRAM)
    print(f"Connecting to {self.defaultTarget}:{self.defaultPort}")
    try:
      message = "Message from client"
      print(f"Sending message: {message}")
      sentMessage = socketEngine.sendto(message.encode("utf-8"),(self.defaultTarget,self.defaultPort))
      data,srv = socketEngine.recvfrom(self.defaultPayload)
      print(f"Received from {srv}:\n{data.decode()}")
    finally:
      print(f"Client has been closed")
      socketEngine.close()

if __name__ == "__main__":
  UDPClient().LaunchClient()