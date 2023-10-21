import socket
from binascii import hexlify,unhexlify

class ConvertIP4(object):
  """
  The two IP addresses have been converted from a string to a 32-bit packet format using a for-in statement
  The function inet_aton() converts an IPv4 address from the dotted-quad string format to 32-bit packed binary format.
  The function inet_ntoa() converts an IP address, which is in 32-bit packed format to the popular human readable dotted-quad string format.

  https://pythontic.com/modules/socket/inet_aton
  https://pythontic.com/modules/socket/inet_ntoa
  """
  def __init__(self):
    self.IPlist = []
  def __str__(self)->str:
    return "Converting IP4"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return ConvertIP4.__doc__
  def CreateTargetIPList(self)->list:
    exampleIPOne = socket.gethostbyname(socket.gethostname())
    self.IPlist.append(exampleIPOne)
    try:
      exampleIPTwo = socket.gethostbyname("www.stackoverflow.com")
      self.IPlist.append(exampleIPTwo)
    except socket.error as socketError:
      print(f"Cannot resolved for www.stackoverflow.com | {socketError}")
  def GetConvertingPackedDefaultIPs(self):
    self.CreateTargetIPList()
    for ipAddress in self.IPlist:
      packedIP = socket.inet_aton(ipAddress)
      print(f"Packed for {ipAddress}: {packedIP}")
  def GetConvertingUnpacked(self,packedIP:str or bytes):
    unpackedIP = socket.inet_ntoa(packedIP)
    print(f"Unpacked for {packedIP}: {unpackedIP}")
  def GetConvertingHex(self,targetPacked:str or bytes):
    unpacked = hexlify(targetPacked)
    print(f"Unpacked to hex for {targetPacked}: {unpacked}")
  def GetConvertingUnhex(self,targetHex:str or bytes):
    unHex = unhexlify(targetHex)
    print(f"Unhex for {targetHex}: {unHex}")

if __name__ == "__main__":
  convertClass = ConvertIP4()
  convertClass.GetConvertingPackedDefaultIPs()
  convertClass.GetConvertingUnpacked(b'h\x12\x17\xc9') #a bytes-like object is required
  convertClass.GetConvertingHex(b'h\x12\x17\xc9') #a bytes-like object is required
  convertClass.GetConvertingHex(b"Hello World") #a bytes-like object is required
  convertClass.GetConvertingUnhex("48656c6c6f20576f726c64")