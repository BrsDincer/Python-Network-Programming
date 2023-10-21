import socket

class GetServiceName(object):
  """
  https://datatracker.ietf.org/doc/html/rfc1340
  https://datatracker.ietf.org/doc/rfc6335/
  https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml/
  """
  def __init__(self):
    self.portDictionary = {
      13:"daytime",
      21:"ftp",
      22:"ssh",
      23:"telnet",
      25:"smtp",
      33:"dsp",
      37:"time",
      42:"nameserver",
      53:"dns",
      80:"http",
      88:"kerberos",
      113:"auth",
      123:"ntp",
      150:"sql-net",
      161:"snmp",
      197:"dls",
      443:"https"
    }
    self.portMethodDictionary = {
      13:"tcp",
      21:"tcp",
      22:"tcp",
      23:"tcp",
      25:"tcp",
      33:"udp",
      37:"udp",
      42:"tcp",
      53:"udp",
      80:"tcp",
      88:"tcp",
      113:"tcp",
      150:"tcp",
      161:"udp",
      197:"udp",
      443:"tcp"
    }
  def __str__(self)->str:
    return "Getting Service Name & Information"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return GetServiceName.__doc__
  def FindByPortType(self):
    for portNumber,portType in self.portMethodDictionary.items():
      try:
        serviceName = socket.getservbyport(portNumber,portType)
        print(f"Service for port {portNumber}: {serviceName} | {portType}")
      except:
        print(f"Not defined for port: {portNumber}")
        pass
  def FindByPortName(self):
    for portNumber,portName in self.portDictionary.items():
      try:
        serviceName = socket.getservbyname(portName)
        print(f"Service for port: {portName}: {serviceName}")
      except:
        print(f"Not defined for port: {portNumber}")
        pass

if __name__ == "__main__":
  GetServiceName().FindByPortType()
  GetServiceName().FindByPortName()