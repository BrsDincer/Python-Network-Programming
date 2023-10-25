import socket,threading,sys,pickle,struct,signal,sys

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

class ChatServer(object):
  def __init__(self):
    self.defaultPort = 12000
    self.defaultHost = ""
    self.defaultUserCount = 5
    self.connections = []
    self.defaultPayload = 2048
  def __str__(self)->str:
    return "Chat Server Base"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return ChatServer.__doc__
  def RemoveConnection(self,socketInit:socket.socket):
    if socketInit in self.connections:
      try:
        socketInit.close()
        self.connections.remove(socketInit)
      except Exception as generalException:
        sys.stdout.write(f"Removing Connection Error: {generalException}")
        pass
    else:
      pass
  def Broadcast(self,message:str,connection:socket.socket):
    for clientConnection in self.connections:
      if clientConnection != connection:
        try:
          SendOps(clientConnection,message.encode())
          #clientConnection.send(message.encode())
        except Exception as err:
          sys.stdout.write(f"Broadcast Error: {err}")
          self.RemoveConnection(clientConnection)
  def HandleUserConnection(self,connection:socket.socket,address:str):
    while True:
      try:
        messagePickle = ReceiveOps(connection)
        #messageFrom = connection.recv(self.defaultPayload)
        if messagePickle:
          sys.stdout.write(f"MESSAGE FROM ADDRESS: {address[0]}:{address[1]}\nMESSAGE: {messagePickle.decode()}\n")
          sys.stdout.flush()
          messageTo = f"FROM {address[0]}:{address[1]} - {messagePickle.decode()}"
          self.Broadcast(messageTo,connection)
        else:
          self.RemoveConnection(connection)
          break
      except Exception as err:
        sys.stdout.write(f"HANDLE ERROR: {str(err)}")
        sys.stdout.flush()
        self.RemoveConnection(connection)
        sys.exit(1)
  def SignalHandler(self,sigNumber,frameTarget):
    if len(self.connections) > 0:
      for connectionInit in self.connections:
        try:
          connectionInit.close()
        except Exception as serr:
          sys.stdout.write(f"SIGNAL ERROR: {serr}")
          sys.stdout.flush()
      sys.stdout.write("CLIENTS HAVE BEEN CLOSED")
      sys.stdout.flush()
    else:
      pass
  def RunServer(self):
    try:
      socketEngine = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      socketEngine.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
      socketEngine.bind((self.defaultHost,self.defaultPort))
      socketEngine.listen(self.defaultUserCount)
      signal.signal(signal.SIGINT,self.SignalHandler)
      sys.stdout.write(f"\nSERVER ON: {socketEngine.getsockname()}\n")
      sys.stdout.flush()
      while True:
        socketClient,socketClientAddress = socketEngine.accept()
        sys.stdout.write(f"CONNECTION FROM {socketClientAddress[0]}:{socketClientAddress[1]}\n")
        sys.stdout.flush()
        self.connections.append(socketClient)
        threading.Thread(target=self.HandleUserConnection,
                         args=[socketClient,socketClientAddress]).start()
        #expThread.setDaemon(True)
    except Exception as err:
      sys.stdout.write(f"\nERROR FOR SOCKET SERVER CLIENT: {str(err)}\n")
      sys.stdout.flush()
    except KeyboardInterrupt:
      sys.stdout.write("\nHAS BEEN CLOSED - SERVER\n")
      sys.stdout.flush()
      if len(self.connections) > 0:
        for initConnection in self.connections:
          self.RemoveConnection(initConnection)
        sys.stdout.write("CLIENT - KILL")
        sys.stdout.flush()
      else:
        pass
      try:
        sys.stdout.write("SERVER - KILL")
        sys.stdout.flush()
        socketEngine.close()
      except:
        pass
    finally:
      if len(self.connections) > 0:
        for initConnection in self.connections:
          self.RemoveConnection(initConnection)
      else:
        pass
      socketEngine.close()

if __name__ == "__main__":
  ChatServer().RunServer()

