import socket

class SendRawGet(object):
  """
  socket.AF_INET: IPv4 (host, port):
    host is a string with a hostname like 'www.example.com' or an IPv4 address like '10.1.2.3'. port is an integer.
  socket.AF_INET6: IPv6 (host, port, flowinfo, scopeid):
    host is a string with a hostname like 'www.example.com' or an IPv6 address like 'fe80::6203:7ab:fe88:9c23'. port is an integer. flowinfo and scopeid represent the sin6_flowinfo and sin6_scope_id members in the C struct sockaddr_in6.
  SOCK_STREAM is the socket type for TCP
  SOCK_DGRAM is the socket type for UDP
  SOCK_RAW is the style that provides access to low-level network protocols and interfaces. Ordinary user programs usually have no need to use this style.
  
  https://www.gnu.org/software/libc/manual/html_node/Sockets.html
  """
  def __init__(self):
    self.targetHost = "www.httpbin.org"
    self.targetPage = "/anything"
    self.targetPort = 80
    self.rawHeader = (
      f"GET {self.targetPage} HTTP/1.1\r\n"
      f"Host: {self.targetHost}\r\n"
      "Content-Type: text/html\r\n"
      "Connection: keep-alive\r\n"
      "Keep-Alive: 155\r\n\r\n"
    )
  def __str__(self)->str:
    return "Sending Raw GET Request"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return SendRawGet.__doc__
  def Run(self):
    try:
      socketEngine = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      socketEngine.settimeout(155)
      print(f"SENDING-HEADER:\n{self.rawHeader}")
      socketEngine.connect((self.targetHost,self.targetPort))
      socketEngine.sendall(self.rawHeader.encode("utf-8"))
      print("DONE\n\n")
      buffer = socketEngine.recv(4096)
      print(f"RESPONSE:\n\n{buffer.decode()}")
      socketEngine.close()
    except:
      try:
        socketEngine.close()
      except:
        pass
if __name__ == "__main__":
  SendRawGet().Run()