import socket,threading

class ForwardingOps(object):
  def __init__(self):
    self.defaultHost = "localhost"
    self.defaultPort = 9950
    self.targetHost = "www.w3.org"
    self.targetPort = 80
    self.defaultPayload = 4096
    self.defaultUserCount = 20
  def __str__(self)->str:
    return "Port Forwarding to Target Host"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return ForwardingOps.__doc__
  def TransferPort(self,sourceInit,destinationInit):
    srcAddr,srcPort = sourceInit.getsockname()
    dstAddr,dstPort = destinationInit.getsockname()
    while True:
      try:
        buffer = sourceInit.recv(self.defaultPayload)
        print(f"\nBUFFER: {buffer}\n")
        if len(buffer) == 0:
          break
        else:
          destinationInit.send(buffer)
      except Exception as err:
        print(f"TRANSFER ERROR: {str(err)}")
        break
    try:
      srcAddr.close()
      dstAddr.close()
    except:
      pass
  def ServerLaunch(self):
    serverEngine = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serverEngine.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    serverEngine.bind((self.defaultHost,self.defaultPort))
    serverEngine.listen(self.defaultUserCount)
    print(f"SERVER ON: {serverEngine.getsockname()}\n")
    while True:
      srcSocket,srcAddress = serverEngine.accept()
      print(f"CONNECTION FROM: {srcAddress}")
      try:
        dstSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        dstSocket.connect((self.targetHost,self.targetPort))
        transferDstSrc = threading.Thread(target=self.TransferPort,
                                          args=[dstSocket,srcSocket])
        transferSrcDst = threading.Thread(target=self.TransferPort,
                                          args=[srcSocket,dstSocket])
        transferDstSrc.start()
        transferSrcDst.start()
      except Exception as err:
        print(f"SERVER ERROR: {str(err)}")

if __name__ == "__main__":
  ForwardingOps().ServerLaunch()
        
