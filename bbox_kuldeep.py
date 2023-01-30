from IPython.lib.display import isdir
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os


path = '/home/santosh/Desktop/prafulla/ball tracking/download/V/Out14/'
path_in = '/home/santosh/Desktop/prafulla/ball tracking/download/V/Frames14/'
aa = os.listdir(path)
for i in aa:
    path1 = path + i
    path1_in = path_in + i
    img = cv2.imread(path1)
    himg,wimg,cimg = img.shape

    # convert to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # threshold
    thresh = cv2.threshold(gray,128,255,cv2.THRESH_BINARY)[1]

    # get contours
    result = img.copy()
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    if len(contours)==0:
        continue
    for cntr in contours:
        x,y,w,h = cv2.boundingRect(cntr)
        #cv2.rectangle(result, (x, y), (x+w, y+h), (0, 0, 255), 2)
        #print("x,y,w,h:",x,y,w,h)
        xc = (x+w/2)/wimg
        yc = (y+h/2)/himg
        wc = w/wimg
        hc = h/himg
    text_path = '/home/santosh/Desktop/prafulla/ball tracking/download/V/Out1_text1/'
    image_in = cv2.imread(path1_in[:-4]+".jpg")
    cv2.imwrite("/home/santosh/Desktop/prafulla/ball tracking/download/V/test1/"+path_in[-8:-1]+i[:-4]+".jpg",image_in)
    if not os.path.isdir(text_path):
        os.makedirs(text_path)
    img_text = text_path + path_in[-8:-1] +i[:-4] +'.txt'
    file1 = open(img_text,"w")
    L = [str(32),' ',str(xc),' ',str(yc),' ',str(wc),' ',str(hc)] 
    file1.writelines(L)
print("done")