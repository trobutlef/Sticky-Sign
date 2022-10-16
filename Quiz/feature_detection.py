# from tkinter import _ScreenUnits
import cv2
from cv2 import waitKey
import numpy as np
import os
from gettext import pgettext
from lib2to3 import pgen2
from tkinter import *
from feature_detection import * 
import pygame as pg
from Settings import *
import subprocess
import numpy as np





class Quiz:

    def __init__(self):
            screen = pg.display.set_mode((WIDTH, HEIGHT))
            pg.display.set_caption('Practice Mode')
            screen.fill(LIGHTPINK)
            pg.display.update()
            
            


    # def show_start_screen(self):
    #         schedreen = pgettext.display.set_mode((700, 700))
    #         pgen2.display.set_caption('Practice Mode')
    #         _ScreenUnits.fill(LIGHTPINK)
    #         pg.display.update()
            pass

orb = cv2.ORB_create(nfeatures=3000)

path = 'train_img/ASL query/'
image = []
classNames = []
myList = os.listdir(path)
quiz_id = np.random.randint(0,len(myList))
thres = 35




# print(myList)
# print("Total classes detected - ", len(myList))



for cl in myList:
    imgCurr = cv2.imread(f'{path}/{cl}',0)
    image.append(imgCurr)
    classNames.append(os.path.splitext(cl)[0])

# print(classNames)

def findDes(images):
    desList = []
    for img in images:
        kp,des = orb.detectAndCompute(img, None)
        desList.append(des)
    return desList

desList = findDes(image)
# print(len(desList))

def findID(img, desList) :
    kp2, des2 = orb.detectAndCompute(img, None)
    bf = cv2.BFMatcher()
    matchList = []
    finalValue = -1
    try:
        for des in desList:
            matches = bf.knnMatch(des,des2,k=2)
            good = []
            for m,n in matches:
                if m.distance < 0.75*n.distance:
                    good.append([m])
            matchList.append(len(good))
    except:
        pass
    if len(matchList) != 0:
        if max(matchList) > thres :
            finalValue = matchList.index(max(matchList))
    return finalValue


cap = cv2.VideoCapture(0)

while True:
    success, img2 = cap.read()
    imgOriginal = img2.copy()
    
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    cv2.putText(imgOriginal,f"What is {classNames[quiz_id]} in ASL??",(50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    id = findID(img2,desList)
    if id != -1:
        # print("hello")
        if id == quiz_id:
            cv2.putText(imgOriginal,"Correct",(200,200), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            waitKey(500)
            cap.release()
        else :
            cv2.putText(imgOriginal,"Try Again",(200,200), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)

    cv2.imshow("img2", imgOriginal)
    waitKey(1)


# ## Getting 5 images to train the model due to time constraints.
# img1 = cv2.imread("train_img/ASL training/A.jpeg", 0)
# img2 = cv2.imread("train_img/ASL training/A_tbm.jpeg ", 0)
# img3 = cv2.imread("train_img/ASL training/C.jpeg", 0)
# img4 = cv2.imread("train_img/ASL training/C_tbm.jpeg", 0)
# img5 = cv2.imread("train_img/ASL training/h.jpeg", 0)
# img6 = cv2.imread("train_img/ASL training/h_tbm.jpeg", 0)
# img7 = cv2.imread("train_img/ASL training/K.jpeg", 0)
# img8 = cv2.imread("train_img/ASL training/k_tbm.jpeg", 0)
# # Testing whether the image is working.

# # cv2.imshow('img1', img8)
# # waitKey(0)

# orb = cv2.ORB_create(nfeatures=3000)

# kp1, des1 = orb.detectAndCompute(img1, None)
# kp2, des2 = orb.detectAndCompute(img2, None)
# kp3, des3 = orb.detectAndCompute(img3, None)
# kp4, des4 = orb.detectAndCompute(img4, None)
# kp5, des5 = orb.detectAndCompute(img5, None)
# kp6, des6 = orb.detectAndCompute(img6, None)
# kp7, des7 = orb.detectAndCompute(img7, None)
# kp8, des8 = orb.detectAndCompute(img8, None)

# # imgKp1 = cv2.drawKeypoints(img1, kp1,None)
# # cv2.imshow('kp1', imgKp1)
# # waitKey(0)

# # print(des1[0])

# bf = cv2.BFMatcher()
# matches = bf.knnMatch(des1,des2,k=2)

# good = []

# for m,n in matches:
#     if m.distance < 0.75*n.distance:
#         good.append([m])

# plott = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)

# # print(len(good))
# # cv2.imshow("img3p", plott)
# # waitKey(0)



