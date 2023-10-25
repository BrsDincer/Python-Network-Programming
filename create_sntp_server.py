import socket,struct,sys,time

class SNTPServer(object):
  """
  Epoch converter:  http://www.epochconverter.com/

  Struct:
  !: network (= big-endian)
  I: unsigned int
  """
  def __init__(self):
    self.defaultPool = "0.uk.pool.ntp.org"
    self.ntpProtocol = 123
    self.time1970 = 2208988800 #epoch - GMT: Sunday, January 1, 2040 12:00:00 AM
    self.sntpRawData = '\x1b'+47*'\0'
  def __str__(self)->str:
    return "Creating SNTP Server"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return SNTPServer.__doc__
  def CreateClient(self):
    clientSocket = socket.socket(socket.AF_INET,
                                 socket.SOCK_DGRAM)
    clientSocket.settimeout(5)
    clientSocket.setblocking(1)
    try:
      clientSocket.sendto(self.sntpRawData.encode("utf-8"),
                          (self.defaultPool,self.ntpProtocol))
      data,addr = clientSocket.recvfrom(1024)
      if data:
        print(f"Received From: {addr} | Pool: {self.defaultPool}")
        unpackData = struct.unpack("!12I",data)
        print(f"Raw Unpack Data: {unpackData}")
        unpackDataTime = unpackData[10]
        print(f"Time Data In Response: {unpackDataTime}")
        unpackDataTime -= self.time1970
        print(f"Raw Time: {unpackDataTime}")
        print(f"TIME: {time.ctime(unpackDataTime)}")
        clientSocket.close()
      else:
        clientSocket.close()
    except:
      try:
        clientSocket.close()
      except:
        clientSocket.close()

if __name__ == "__main__":
  SNTPServer().CreateClient()
