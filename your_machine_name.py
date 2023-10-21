import socket

class HostNamePrinting(object):
  """
  The hostname is what you assigned to your computer when you configured your operating system.
  """
  def __init__(self):
    self.hostName = socket.gethostname()
    # help(socket.gethostname)
    self.ipAddress = socket.gethostbyname(self.hostName)
    # help(socket.gethostbyname)
  def __str__(self)->str:
    return "Host Name Printing"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplemented(NotImplementedError)
  def __repr__(self)->str:
    return HostNamePrinting.__doc__
  
if __name__ == "__main__":
  hostName = HostNamePrinting().hostName
  ipAddress = HostNamePrinting().ipAddress
  print(f"Host Name: {hostName}")
  print(f"IP Address: {ipAddress}")