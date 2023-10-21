import socket

class RemoteMachineIP(object):
  def __init__(self):
    self.exampleHost = "www.stackoverflow.com"
  def __str__(self)->str:
    return "Remote Machine IP Information"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return RemoteMachineIP.__doc__
  def GetIP(self)->str:
    try:
      targetIP = socket.gethostbyname(self.exampleHost)
      print(f"Target IP: {targetIP} | {self.exampleHost}")
    except socket.error as socketError:
      print(f"ERROR: {socketError} / FOR: {self.exampleHost}")

if __name__ == "__main__":
  RemoteMachineIP().GetIP()