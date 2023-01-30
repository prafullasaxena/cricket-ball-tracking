import os
import glob
images_names = sorted(glob.glob("test1/*.jpg"))
for i in images_names:
    command = "python detect.py --weights runs/train/exp7/weights/best.pt --source "+ i
    os.system(command)

