import cv2
import numpy as np
import os

path=".\imagequery"
print("imagers are::",path)
orb = cv2.ORB_create(nfeatures=2000)

#---------Import Images----------------
images=[]
classnames=[]
mylist=os.listdir(path)
print(mylist)
print("total classes detected=",len(mylist))

#import images one by one
for cl in mylist:
     imgcur=cv2.imread(f'{path}/{cl}',0)
     images.append(imgcur)
     classnames.append(os.path.splitext(cl)[0])
print(classnames)

#get descripter after scanning

def finddes(images):
    deslist=[]
    for img in images:
        kp,des=orb.detectAndCompute(img,None)
        # print(des)
        deslist.append(des)
    return deslist

def findID(img,deslist,thres=15):
    kp2,des2=orb.detectAndCompute(img,None)
    # print("input",des2)
    bf = cv2.BFMatcher()
    matchlist=[]

    finalval=-1
    try:
        for des in deslist:
            matches=bf.knnMatch(des,des2,k=2)
            good = []
            for m,n in matches:
                if m.distance<0.75 * n.distance:
                    good.append([m])
            matchlist.append(len(good))
    except:
        pass
    #print(matchlist)
    if len(matchlist)!=0:
        if max(matchlist) > thres:
            finalval=matchlist.index(max(matchlist))
    return finalval


deslist=finddes(images)
#print(len(deslist))

#camera

cap=cv2.VideoCapture(0)
#print(cap,"capp")

while True:
    

    success,img2 =cap.read()

   # print(cap.read(),"qwerty")
    #print("image is", img2)
    imgoriginal=img2.copy()

    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

    id=findID(img2,deslist)
    if id!=-1:
        cv2.putText(imgoriginal,classnames[id],(100,100),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)

    cv2.imshow('Scanner',imgoriginal)
    cv2.waitKey(100)



    # #cv2.imshow('img2',img2)
    # if cv2.waitKey(0) & 0xFF == 46:
    #     break
    #     cv2.destroyAllWindows()
    # cap.release()



