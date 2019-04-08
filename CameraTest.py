import cv2
import numpy as np
import urllib.request 
import numpy as np
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
url = "http://192.168.43.99/cgi-bin/snapshot.cgi"
password_mgr.add_password(None, url, "admin", "mycamera2")
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
while True:
  info = opener.open(url).read()
  imgNp=np.array(bytearray(info),dtype=np.uint8)
  frame=cv2.imdecode(imgNp,-1)
  cv2.imshow('Frame',frame)
  if cv2.waitKey(25) & 0xFF == ord('q'):
    break

cv2.destroyAllWindows()
