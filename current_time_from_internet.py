import ntplib
from time import ctime

class NtpTimeGathering(object):
  """
  https://github.com/cf-natali/ntplib/blob/master/ntplib.py : Source Code
  https://techhub.hpe.com/eginfolib/networking/docs/switches/5120si/cg/5998-8503_nmm_cg/content/436051971.htm : NTP Modes
  https://www.ntppool.org/zone : Pools
  """
  def __init__(self):
    self.defaultPool = "0.europe.pool.ntp.org"
  def __str__(self)->str:
    return "Network Time Protocol (NTP) - Internet Time Server"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self):
    return NtpTimeGathering.__doc__
  def GetTime(self):
    ntpClient = ntplib.NTPClient()
    response = ntpClient.request(self.defaultPool)
    print(f"Mode: {response.mode}")
    print(f"Leap: {ntplib.leap_to_text(response.leap)}")
    print(f"Delay: {response.delay}")
    print(f"Raw Time: {response.tx_time}")
    print(f"Root Delay: {response.root_delay}")
    timeServer = ctime(response.tx_time)
    print(f"Time: {timeServer}")

if __name__ == "__main__":
  NtpTimeGathering().GetTime()
