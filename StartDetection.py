import DbOperations
import cv2
import threading
import FaceRecognition
import urllib.request
import numpy as np
import tkinter as tk

def main(cameraIp, userName, password, cameraType):
    global isRunning,RecognitionObj
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    url = cameraIp
    password_mgr.add_password(None, url, userName, password)
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(handler)
    while isRunning:
        info = opener.open(url).read()
        imgNp=np.array(bytearray(info),dtype=np.uint8)
        frame=cv2.imdecode(imgNp,-1)
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        PredictedUsers = RecognitionObj.PredictUsers(frame_gray)
        print(PredictedUsers)
        for Label,Accuracy,x,y,w,h in PredictedUsers:
            if(Accuracy<thresholdAccuracy):
                if(cameraType=="In"):
                    db.insertInTime(Label)
                else:
                    db.insertOutTime(Label)
    cv2.destroyAllWindows()

def trainNewUsers():
    rows = db.getNewEmployeeImageDir()
    print(rows)

db = DbOperations.DbOperations("attendancemanagementsystem")
isRunning = True
thresholdAccuracy = 80
RecognitionObj = FaceRecognition.FaceRecognition("Models/haarcascade_frontalface_default.xml","Models/FaceRecognition.xml")
threading.Thread(target=main,args=("http://192.168.43.99/cgi-bin/snapshot.cgi","admin","mycamera2",'In')).start()
threading.Thread(target=main,args=("http://192.168.43.98/cgi-bin/snapshot.cgi","admin","mycamera1",'Out')).start()
root = tk.Tk()
root.geometry("100x100")
root.resizable(0, 0)
ButtonTrain = tk.Button(root,text="Train",command=trainNewUsers)
ButtonTrain.grid(row=0,column=0,sticky=tk.W+tk.N+tk.S+tk.E)
root.mainloop()









































