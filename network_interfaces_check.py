import sys,socket,fcntl,struct,array

class NetworkInterfaces(object):
  """
  Use for UNIX: LINUX
  """
  def __init__(self):
    self.siocgifconfiguration = 0x8912 #35090
    self.size32 = 32
    self.size64 = 40
    self.platform32MaxNumber = 2**32
    self.defaultInterfaces = 8
  def __str__(self)->str:
    return "List Network Interfaces"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return NetworkInterfaces.__doc__
  def ListAll(self):
    interfaceList = []
    maxInterfaceCount = self.defaultInterfaces
    bit64Control = sys.maxsize > self.platform32MaxNumber
    structSize = self.size64 if bit64Control else self.size32
    socketEngine = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True:
      bytesAll = maxInterfaceCount * structSize
      interfaceName = array.array("B",b"\0"*bytesAll)
      socketInfo = fcntl.ioctl(socketEngine.fileno(),
                               self.siocgifconfiguration,
                               struct.pack("iL",
                                           bytesAll,
                                           interfaceName.buffer_info()[0]))
      outBytes = struct.unpack("iL",socketInfo)[0]
      if outBytes == bytesAll:
        maxInterfaceCount *= 2
      else:
        break
    name = interfaceName.tostring()
    for init in range(0,outBytes,structSize):
      interfaceList.append((name[init:init+16].split(b"\0",1)[0]).decode("ascii","ignore"))
    return interfaceList
  
if __name__ == "__main__":
  interfaces = NetworkInterfaces().ListAll()
  print(f"MACHINE-NETWORK INTERFACES:\nTOTAL:{len(interfaces)}\nLIST:{interfaces}")