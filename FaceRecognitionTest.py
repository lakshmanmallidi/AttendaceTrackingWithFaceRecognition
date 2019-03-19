import FaceRecognition
import cv2
Obj = FaceRecognition.FaceRecognition("","Models/haarcascade_frontalface_default.xml")
Obj.TrainUser('Images/1',100)
Obj.TrainUser('Images/2',201)
Obj.TrainUser('Images/3',31)
print(Obj.PredictUsers(cv2.imread('Images/p1.jpg',0)))
print(Obj.PredictUsers(cv2.imread('Images/p3.jpg',0)))
print(Obj.PredictUsers(cv2.imread('Images/p2.jpg',0)))
print(Obj.PredictUsers(cv2.imread('F:/photos/x.jpg',0)))

