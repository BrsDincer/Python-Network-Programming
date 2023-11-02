import asyncore,socket
#The asyncore module is deprecated and will be removed in Python 3.12. The recommended replacement is asyncio.


class ReceiverOps(asyncore.dispatcher):
  def __init__(self,conn):
    asyncore.dispatcher.__init__(self,conn)
    self.from_remote_buffer = b""
    self.to_remote_buffer = b""
    self.sender = None
  def __str__(self)->str:
    return "Receiver Class Design"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return ReceiverOps.__doc__
  def handle_connect(self):
    pass
  def handle_read(self):
    read = self.recv(4096)
    self.from_remote_buffer += read
  def writable(self):
    return (len(self.to_remote_buffer) > 0)
  def handle_write(self):
    sent = self.send(self.to_remote_buffer)
    self.to_remote_buffer = self.to_remote_buffer[sent:]
  def handle_close(self):
    self.close()
    if self.sender:
      self.sender.close()

class SenderOps(asyncore.dispatcher):
  def __init__(self,receiver,remoteaddr,remoteport):
    asyncore.dispatcher.__init__(self)
    self.receiver = receiver
    receiver.sender = self
    self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
    self.connect((remoteaddr,remoteport))
  def __str__(self)->str:
    return "Sender Class Design"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplementedError)
  def __repr__(self)->str:
    return SenderOps.__doc__
  def handle_connect(self):
    pass
  def handle_read(self):
    read = self.recv(4096)
    print(f"\->RECEIVED REMOTE BUFFER:\n{read}\n")
    self.receiver.to_remote_buffer += read
    print(f"\nTO REMOTE BUFFER:\n{self.receiver.to_remote_buffer.decode()}\n")
  def writable(self):
    return (len(self.receiver.from_remote_buffer) > 0)
  def handle_write(self):
    sent = self.send(self.receiver.from_remote_buffer)
    print(f"\->SENT REMOTE BUFFER:\n{self.receiver.from_remote_buffer.decode()}\n")
    self.receiver.from_remote_buffer = self.receiver.from_remote_buffer[sent:]
    print(f"\nFROM REMOTE BUFFER:\n{self.receiver.from_remote_buffer.decode()}\n")
  def handle_close(self):
    self.close()
    self.receiver.close()

class PortForwarding(asyncore.dispatcher):
  def __init__(self,ip,port,remoteip,remoteport,backlog=5):
    asyncore.dispatcher.__init__(self)
    self.remoteip = remoteip
    self.remoteport = remoteport
    self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
    self.set_reuse_addr()
    self.bind((ip,port))
    self.listen(backlog)
    print(f"LISTENING ON: {ip}:{port}")
  def __str__(self)->str:
    return "Port Forwarding ASYNCORE"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def handle_accept(self):
    connection,addr = self.accept()
    print(f"CONNECTION FROM: {addr}")
    SenderOps(ReceiverOps(connection),
              self.remoteip,
              self.remoteport)

if __name__ == "__main__":
  defaultHost = "localhost"
  defaultPort = 12532
  targetHost = "google.com"
  targetPort = 80
  PortForwarding(ip=defaultHost,port=defaultPort,remoteip=targetHost,remoteport=targetPort)
  asyncore.loop()