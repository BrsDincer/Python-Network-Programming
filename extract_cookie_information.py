import http.cookiejar,urllib

class ExtractionOps(object):
  def __init__(self):
    self.userId = "id_username"
    self.userPassword = "id_password"
    self.username = "you@email.com" #change
    self.password = "mypassword" #change
    self.loginURL = "https://bitbucket.org/account/signin/?next=/"
    self.normalURL = "https://bitbucket.org/"
  def __str__(self)->str:
    return "Extraction Cookie Information"
  def __call__(self)->None:
    return None
  def __getstate__(self):
    raise NotImplementedError(NotImplemented)
  def __repr__(self)->str:
    return ExtractionOps.__doc__
  def Extract(self):
    cookieJAR = http.cookiejar.CookieJar()
    loginData = urllib.parse.urlencode({self.userId:self.username,
                                        self.userPassword:self.password}).encode("utf-8")
    print(f"LOGIN FORMAT DATA:\n{loginData}")
    openerOPS = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookieJAR))
    response = openerOPS.open(self.loginURL,loginData)
    for c_ in cookieJAR:
      print(f"FIRST COOKIE:\n{c_.name}: {c_.value}")
    print(f"\nTOTAL HEADER-FIRST:\n{response.header}\n")
    responseActive = openerOPS.open(self.normalURL)
    for c_ in cookieJAR:
      print(f"SECOND COOKIE:\n{c_.name}: {c_.value}")
    print(f"\nTOTAL HEADER-SECOND:\n{responseActive.header}")

if __name__ == "__main__":
  ExtractionOps().Extract()