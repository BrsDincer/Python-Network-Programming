import socket,threading,pickle,struct,sys

def SendOps(channel,*args):
  buffer = pickle.dumps(args)
  value = socket.htonl(len(buffer))
  size = struct.pack("L",value)
  channel.send(size)
  channel.send(buffer)

def ReceiveOps(channel):
  size = struct.calcsize("L")
  size = channel.recv(size)
  try:
    size = socket.ntohl(struct.unpack("L",size)[0])
  except struct.error as serrt:
    return ""
  buff = ""
  while len(buff) < size:
    buff = channel.recv(size-len(buff))
  return pickle.loads(buff)[0]

class ChatClient(object):
  def __init__(self):
    self.defaultHost = "127.0.0.1"
    self.defaultPort = 12000
    self.defaultPayload = 2048
  def __str__(self)->str:
    return "Chat Client Base"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return ChatClient.__doc__
  def HandleMessage(self,connection:socket.socket):
    while True:
      try:
        messagePickle = ReceiveOps(connection)
        #messageFrom = connection.recv(self.defaultPayload)
        if messagePickle:
          sys.stdout.write(f"\nMESSAGE:\n{messagePickle.decode()}\n")
          sys.stdout.flush()
        else:
          connection.close()
          break
      except Exception as err:
        sys.stdout.write(f"\nERROR: {str(err)}\n")
        sys.stdout.flush()
        break
  def RunClient(self):
    try:
      socketEngine = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      socketEngine.connect((self.defaultHost,self.defaultPort))
      threading.Thread(target=self.HandleMessage,
                       args=[socketEngine]).start()
      #expThread.setDaemon(True)
      sys.stdout.write("\nCONNECTION HAS BEEN STARTED\n")
      sys.stdout.flush()
      while True:
        messageInit = sys.stdin.readline().strip()
        sys.stdout.flush()
        if messageInit.lower() == "quit":
          sys.stdout.write("\nCONNECTION HAS BEEN CLOSED - QUIT\n")
          sys.stdout.flush()
          break
        else:
          pass
        SendOps(socketEngine,messageInit.encode())
        #socketEngine.send(messageInit.encode())
      try:
        socketEngine.close()
      except:
        pass
    except Exception as err:
      sys.stdout.write(f"\nCONNECTION ERROR: {str(err)}\n")
      sys.stdout.flush()
      try:
        socketEngine.close()
      except:
        pass

if __name__ == "__main__":
  ChatClient().RunClient()