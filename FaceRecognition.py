import cv2
import os
import numpy as np
import warnings
class FaceRecognition:   
    def __init__(self,FaceDetectorModelPath,FaceRecognizerModelPath=""):
        if(os.path.isfile(FaceDetectorModelPath)):
            self.__FaceRecognizer = None
            self.__FaceDetector = cv2.CascadeClassifier(FaceDetectorModelPath)
            self.__FaceRecognizerModelPath = FaceRecognizerModelPath
            if(os.path.isfile(FaceRecognizerModelPath)):
                self.load()
            elif(FaceRecognizerModelPath != ""):
                self.__FaceRecognizer = cv2.face.LBPHFaceRecognizer_create()
                self.save()
        else:
            raise Exception('No FaceDetectorModel exists')
    
    def save(self):
        self.__FaceRecognizer.save(self.__FaceRecognizerModelPath)
    
    def load(self):
        del(self.__FaceRecognizer)
        self.__FaceRecognizer = cv2.face.LBPHFaceRecognizer_create()
        self.__FaceRecognizer.read(self.__FaceRecognizerModelPath)
    
    def TrainUser(self, FolderPath, UserId):
        ImagePaths = [FolderPath+"/"+EachFile for EachFile in os.listdir(FolderPath) if os.path.isfile(FolderPath+"/"+EachFile)]
        Labels = []
        Cv2Images = []
        for path in ImagePaths:
            try: 
                Img=cv2.imread(path,0)
                Faces = self.__FaceDetector.detectMultiScale(Img, 1.3, 5)
                if(len(Faces)==1):
                    x,y,w,h=Faces[0]
                    ROI_gray = Img[y:y+h, x:x+w]
                    ResizedImg=cv2.resize(ROI_gray,(128,128))
                    Cv2Images.append(ResizedImg)
                    Labels.append(UserId)
            except Exception as e:
                warning.warn("Improper Image format: "+path)
        self.__FaceRecognizer.update(Cv2Images,np.array(Labels))
        self.save()
        #self.load()
            
    def ReTrainAllUsers(self, FolderPaths, UserIds):
        AllImagePaths = []
        Labels = []
        for i in range(len(FolderPaths)):
            ImagePaths = [FolderPaths[i]+"/"+EachFile for EachFile in os.listdir(FolderPaths[i]) if os.path.isfile(FolderPaths[i]+"/"+EachFile)]
            AllImagePaths = AllImagePaths + ImagePaths
            Labels = Labels + [UserIds for _ in range(len(ImagePaths))]
        Cv2Images = []
        for path in ImagePaths:
            try:
                Img=cv2.imread(path,0)
                Faces = self.__FaceDetector.detectMultiScale(Img, 1.3, 5)
                if(len(Faces)==1):
                    x,y,w,h=Faces[0]
                    ROI_gray = Img[y:y+h, x:x+w]
                    ResizedImg=cv2.resize(ROI_gray,(128,128))
                    Cv2Images.append(ResizedImg)
            except Exception as e:
                warning.warn("Improper Image format: "+path)
        self.__FaceRecognizer.train(Cv2Images,np.array(Labels))
        self.save()
        #self.load()
        
    def PredictUsers(self, Frame):
        Faces = self.__FaceDetector.detectMultiScale(Frame, 1.3, 5)
        PredictedUsers = []
        for (x,y,w,h) in Faces:
            ROI_gray = Frame[y:y+h, x:x+w]
            ResizedImg=cv2.resize(ROI_gray,(128,128))
            Label, Accuracy =self.__FaceRecognizer.predict(ResizedImg)
            PredictedUsers.append([Label, Accuracy, x, y, w, h])
        return PredictedUsers
