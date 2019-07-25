"""

Designed and Developed by-
Udayraj Deshmukh 
https://github.com/Udayraj123

"""
import glob
import cv2
import re
import os

# 1: View without saving, 2: Save files without showing
review=0;

dir_glob ='*/*.jpg'

def move(filepath,filepath2,out=True):
    if(filepath==filepath2):return
    if(os.path.exists(filepath)):
        if(os.path.exists(filepath2)):
            print('ERROR : Duplicate file at ' + filepath2)
            exit(0)
        if(review):
            if(out):
                print("Dummy move:",filepath2, '\t',filepath)
            return
        else:
            os.rename(filepath,filepath2)
            if(out):print(filepath2, '\t',filepath)
    else:
        if(out):print('File already moved!', filepath2, filepath)
        exit(0)
allOMRs= list(glob.iglob(dir_glob))
print("Total",len(allOMRs))

for filepath in allOMRs:
    # J_02777.jpg
    finder = re.search(r'(.*/.*_)(.*)\.jpg',filepath,re.IGNORECASE)
    if(finder):
        prefix = finder.group(1)
        counter = int(finder.group(2))
        move(filepath, prefix+format(counter,"05d")+".jpg")
    else:
        print("Unexpected filepath", filepath)
        exit(0)