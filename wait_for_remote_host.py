import socket,errno
from time import time

class NetServiceChecker(object):
  def __init__(self):
    self.defaultHost = "localhost"
    self.defaultPort = 9900
    self.timeout = 100
    self.socketEngine = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  def __str__(self)->str:
    return "Service Connection Checking"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return NetServiceChecker.__doc__
  def CloseWaiting(self):
    try:
      self.socket.close()
    except:
      pass
  def CheckConnection(self):
    if self.timeout:
      endTime = time()+self.timeout
    else:
      pass
    while True:
      try:
        if self.timeout:
          nextTimeout = endTime - time()
          if nextTimeout < 0:
            return False
          else:
            print(f"\nNEXT TIMEOUT CONFIGURATION: {round(nextTimeout)}")
            self.socketEngine.settimeout(nextTimeout)
        else:
          pass
        self.socketEngine.connect((self.defaultHost,self.defaultPort))
      except socket.timeout as terr:
        if self.timeout:
          return False
        else:
          pass
      except socket.error as serr:
        print("TARGET IS CLOSED/CHECKING...\n")
      else:
        self.CloseWaiting()
        return True
      
if __name__ == "__main__":
  serviceCheckerBool = NetServiceChecker().CheckConnection()
  if serviceCheckerBool:
    print("SERVICE IS OKAY NOW")