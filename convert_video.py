import cv2
import numpy as np
import glob

images_names = sorted(glob.glob("runs/detect/detections/*.jpg"))
img=[]
for i in images_names:
    img.append(cv2.imread(i))

height,width,layers=img[1].shape

#fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')

#video=cv2.VideoWriter('video.mp4',-1,1,(width,height))
video=cv2.VideoWriter('unseen_output_video.mp4',fourcc,15,(width,height))

for j in img:
    video.write(j)

cv2.destroyAllWindows()
video.release()