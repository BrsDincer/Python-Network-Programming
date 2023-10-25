import socket

class TCPEchoClient(object):
  def __init__(self):
    self.defaultHost = "localhost"
    self.defaultPort = 9900
    self.defaultPayload = 2048
  def __str__(self)->str:
    return "TCP Echo Client"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return TCPEchoClient.__doc__
  def LaunchClient(self):
    socketEngine = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print(f"Connecting to {self.defaultHost}:{self.defaultPort}")
    socketEngine.connect((self.defaultHost,self.defaultPort))
    try:
      message = "Echo Message Test"
      print("Sending message to server")
      socketEngine.sendall(message.encode("utf-8"))
      amount = 0
      amountExpected = len(message)
      while amount < amountExpected:
        data = socketEngine.recv(self.defaultPayload)
        amount += len(data)
        print(f"RECEIVED FROM SERVER: {data}")
    except socket.error as err:
      print(f"Socket Error: {err}")
    except Exception as epp:
      print(f"General Exception: {epp}")
    finally:
      print("Closing...")
      socketEngine.close()

if __name__ == "__main__":
  TCPEchoClient().LaunchClient()