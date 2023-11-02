import time,sched
from scapy.all import sr,srp,IP,UDP,ICMP,TCP,ARP,Ether

class DetectionInactiveMachine(object):
  def __init__(self,targetHosts):
    self.targetHosts = targetHosts
    self.scheduler = sched.scheduler(time.time,time.sleep)
    self.frequency = 10
  def __str__(self)->str:
    return "Detection Inactive Machines"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return DetectionInactiveMachine.__doc__
  def Detect(self):
    self.scheduler.enter(self.frequency,
                         1,
                         self.Detect,
                         (self.targetHosts,))
    inactiveHosts = []
    try:
      ans,unans = sr(IP(dst=self.targetHosts)/ICMP(),retry=0,timeout=1)
      ans.summary(lambda s,r:r.sprintf("%IP.src% IS ALIVE"))
      for inactives in unans:
        print(f"INACTIVE MACHINE IP: {inactives.dst}")
        inactiveHosts.append(inactives.dst)
      print(f"TOTAL INACTIVE MACHINES: {len(inactiveHosts)}")
    except Exception as err:
      print(f"GENERAL ERROR: {str(err)}")
    except KeyboardInterrupt:
      exit(0)

if __name__ == "__main__":
  detectInactive = DetectionInactiveMachine("www.slashdot.org/30")
  detectInactive.Detect()

