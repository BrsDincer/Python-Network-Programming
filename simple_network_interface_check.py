from ctypes import *

class Sockaddr(Structure):
  _fields_ = [("sa_family",c_ushort),
              ("sa_data",c_char*14)]
class Ifa_Ifu(Union):
  _fields_ = [("ifu_broadcast",POINTER(Sockaddr)),
              ("ifu_dstaddr",POINTER(Sockaddr))]
class Ifaddrs(Structure):
  pass
Ifaddrs._fields_ = [("ifa_next",POINTER(Ifaddrs)),
                    ("ifa_name",c_char_p),
                    ("ifa_netmask",POINTER(Sockaddr)),
                    ("ifa_ifu",Ifa_Ifu),
                    ("ifa_data",c_void_p)]
def GetAllInterfaces():
  libc = CDLL("libc.so.6")
  libc.getifaddrs.restype = c_int
  ifaddr_p = pointer(Ifaddrs())
  ret = libc.getifaddrs(pointer((ifaddr_p)))
  interfaces = set()
  headInfo = ifaddr_p
  while ifaddr_p:
    interfaces.add(ifaddr_p.contents.ifa_name)
    ifaddr_p = ifaddr_p.contents.ifa_next
  libc.freeifaddrs(headInfo)
  return interfaces

if __name__ == "__main__":
  print(GetAllInterfaces())
