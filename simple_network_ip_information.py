import netaddr as na

class NetworkIPInformation(object):
  def __init__(self,testIP:str):
    self.testIP = testIP
  def __str__(self)->str:
    return "Information Based on IP and Network"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return NetworkIPInformation.__doc__
  def GetGeneral(self):
    ipBase = na.IPNetwork(str(self.testIP))
    ip = ipBase.ip
    ipBits = ip.bits()
    network = ipBase.network
    broadcast = ipBase.broadcast
    version = ipBase.version
    prefixLen = ipBase.prefixlen
    netMask = ipBase.netmask
    hostMask = ipBase.hostmask
    ipSize = ipBase.size
    ipValue = ipBase.value
    print(f"IP Bits Representation: {ipBits}")
    print(f"IP Address: {ip}")
    print(f"Network: {network}")
    print(f"Broadcast: {broadcast}")
    print(f"Versino: {version}")
    print(f"Prefix Length: {prefixLen}")
    print(f"Net Mask: {netMask}")
    print(f"Host Mask: {hostMask}")
    print(f"Size: {ipSize}")
    print(f"IP Value: {ipValue}")

if __name__ == "__main__":
  targetIP = "192.168.1.56"
  ipControl = NetworkIPInformation(targetIP)
  ipControl.GetGeneral()
