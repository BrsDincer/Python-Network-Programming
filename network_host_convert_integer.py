import socket

class ConvertInteger(object):
  """
  (ntohl-ntohs,htonl-htons): 'n' represents network and 'h' represents host; 'l' represents long(32) and 's' represents short(16)

  ntohl() function converts a 32 bit integer from network order to host order.
  htonl() function converts a 32 bit positive integer from host byte order to network byte order.
  ntohs() function of socket module converts a 16 bit integer from network format to host format.
  htons() function converts a 16 bit positive integer from host byte order to network byte order.
  """
  def __init__(self):
    self.exampleData = 3452
  def __str__(self)->str:
    return "32bit & 16bit Host-Network Byte Order"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return ConvertInteger.__doc__
  def Get32(self):
    hostOrder = socket.ntohl(self.exampleData)
    networkOrder = socket.htonl(self.exampleData)
    print(f"Original Integer Data: {self.exampleData} | 32-Host: {hostOrder}, 32-Network: {networkOrder}")
  def Get16(self):
    hostOrder = socket.ntohs(self.exampleData)
    networkOrder = socket.htons(self.exampleData)
    print(f"Original Integer Data: {self.exampleData} | 16-Host: {hostOrder}, 16-Network: {networkOrder}")

if __name__ == "__main__":
  ConvertInteger().Get32()
  ConvertInteger().Get16()