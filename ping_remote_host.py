import os,socket,struct,select,time

class PingOps(object):
  def __init__(self,
               targetHost,
               defaultCount=4,
               defaultTimeout=2):
    self.targetHost = targetHost
    self.count = defaultCount
    self.timeout = defaultTimeout
    self.defaultPayload = 2048
    self.icmpEchoRequest = 8
  def __str__(self)->str:
    return "Ping to host"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return PingOps.__doc__
  def ChecksumControl(self,sourceString):
    """
    https://stackoverflow.com/questions/55218931/calculating-checksum-for-icmp-echo-request-in-python
    """
    sumTotal = 0
    maxCount = (len(sourceString)/2)*2
    count = 0
    while count < maxCount:
      valueTarget = sourceString[count + 1]*256 + sourceString[count]
      sumTotal += valueTarget
      sumTotal = sumTotal & 0xffffffff
      count += 2
    if maxCount < len(sourceString):
      sumTotal += ord(sourceString[len(sourceString) - 1])
      sumTotal = sumTotal & 0xffffffff
      # 0xffffffff = -1 or 4294967295
      # AND: &
    else:
      pass
    sumTotal = (sumTotal >> 16) + (sumTotal & 0xffff)
    # 0xffff = 65535
    # sumTotal >> 16  # shift right by 16 bits
    sumTotal = sumTotal + (sumTotal >> 16)
    # sumTotal >> 16  # shift right by 16 bits
    answer = ~sumTotal
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    # 0xff00 = 65280
    # answer >> 8  # shift right by 8 bits
    # answer << 8  # shift left by 8 bits
    # OR: |
    return answer
  def ReceiveResponsePong(self,socketTarget,idTarget,timeout):
    timeRemain = timeout
    while True:
      startTime = time.time()
      readable = select.select([socketTarget],[],[],timeRemain)
      timeSpent = ((time.time() - startTime))
      if readable[0] == []:
        return
      timeReceived = time.time()
      recvPacket,addr = socketTarget.recvfrom(self.defaultPayload)
      ICMPHeader = recvPacket[20:28]
      typeOut,codeOut,checksum,packetID,sequence = struct.unpack("bbHHh",ICMPHeader)
      if packetID == idTarget:
        bytesInDouble = struct.calcsize("d")
        timeSent = struct.unpack("d",recvPacket[28:28+bytesInDouble])[0]
        return timeReceived - timeSent
      else:
        pass
      timeRemain = timeRemain - timeSpent
      if timeRemain <= 0:
        return
  def SendPing(self,socketTarget,idTarget):
    targetAddr = socket.gethostbyname(self.targetHost)
    print(f"TARGET IP: {targetAddr}")
    myChecksum = 0
    header = struct.pack("bbHHh",self.icmpEchoRequest,0,myChecksum,idTarget,1)
    bytesInDouble = struct.calcsize("d")
    data = (192-bytesInDouble)*"Q"
    data = struct.pack("d",time.time())+bytes(data.encode("utf-8"))
    myChecksum = self.ChecksumControl(header+data)
    header = struct.pack("bbHHh",self.icmpEchoRequest,0,socket.htons(myChecksum),idTarget,1)
    packet = header + data
    socketTarget.sendto(packet,(targetAddr,1))
    print(f"\n SENT-PACKET: {packet}\n")
  def PingOnce(self):
    icmp = socket.getprotobyname("icmp")
    print(f"ICMP PROTOCOL: {icmp}")
    try:
      socketEngine = socket.socket(socket.AF_INET,socket.SOCK_RAW,icmp)
    except Exception as err:
      print(f"ICMP SOCKET ERROR: {str(err)}")
    myID = os.getpid() & 0xFFFF
    self.SendPing(socketTarget=socketEngine,idTarget=myID)
    delayTarget = self.ReceiveResponsePong(socketTarget=socketEngine,idTarget=myID,timeout=self.timeout)
    try:
      socketEngine.close()
    except:
      pass
    return delayTarget
  def PingLaunch(self):
    for init in range(self.count):
      print(f"PING - TARGET: {self.targetHost}")
      try:
        delay = self.PingOnce()
      except socket.gaierror as gerr:
        print(f"\nPING FAILED: {str(gerr)}\n")
        break
      if delay == None:
        print(f"\nPING FAILED - DUE TO TIMEOUT: WITHIN {self.timeout}\n")
      else:
        delay = delay * 1000
        print("GET PONG - IN %0.4f ms\n"%delay)

if __name__ == "__main__":
  target = "www.google.com"
  pingOpsEngine = PingOps(targetHost=target)
  pingOpsEngine.PingLaunch()
