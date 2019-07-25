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

inputs_dir ='inputs/OMR_Files/'
filtered_dir ='inputs/filtered/'
dir_glob ='outputs/CheckedOMRs/*/*.jpg'

counter = 0
GENUINES = set(["H_01898.jpg", "H_01899.jpg", "H_01900.jpg", "H_01901.jpg", "H_01902.jpg", "H_01904.jpg", "H_01905.jpg", "H_01906.jpg", "H_01907.jpg", "H_01909.jpg", "H_01910.jpg", "H_01911.jpg", "H_01912.jpg", "H_01913.jpg", "H_01914.jpg", "H_01916.jpg", "H_01918.jpg", "H_01920.jpg", "H_01921.jpg", "H_01922.jpg", "H_01924.jpg", "H_05803.jpg", "H_05804.jpg", "H_05805.jpg", "H_05806.jpg", "H_05807.jpg", "H_05808.jpg", "H_05809.jpg", "H_05810.jpg", "H_05811.jpg", "H_05812.jpg", "H_05813.jpg", "H_05814.jpg", "H_05815.jpg", "H_11729.jpg", "J_02925.jpg", "J_02926.jpg", "J_02927.jpg", "J_02928.jpg", "J_02929.jpg", "J_02930.jpg", "J_02931.jpg", "J_02932.jpg", "J_02933.jpg", "J_02934.jpg", "J_02935.jpg", "J_02936.jpg", "J_02937.jpg", "J_02938.jpg", "J_02939.jpg", "J_02940.jpg", "J_02941.jpg", "J_02942.jpg", "J_02944.jpg", "J_02945.jpg", "J_02946.jpg", "J_02947.jpg", "J_02948.jpg", "J_02949.jpg", "J_02950.jpg", "J_02951.jpg", "J_02952.jpg", "J_02953.jpg", "J_02954.jpg", "J_02955.jpg", "J_02956.jpg", "J_03079.jpg", "J_04136.jpg", "J_05782.jpg", "J_05783.jpg", "J_07576.jpg", "J_08146.jpg", "J_08147.jpg", "J_08148.jpg", "J_11692.jpg", "J_11694.jpg", "J_11701.jpg", "J_11702.jpg", "J_11707.jpg", "J_11711.jpg", "J_11713.jpg"])
MOTHER_OF_GODS = set(["H_09349.jpg", "H_07380.jpg", "H_07282.jpg", "H_14094.jpg", "H_07279.jpg", "H_14125.jpg", "H_11716.jpg", "H_11717.jpg", "H_11718.jpg", "H_11719.jpg", "H_11720.jpg", "H_11721.jpg", "H_11722.jpg", "H_11723.jpg", "H_11724.jpg", "H_11725.jpg", "H_11726.jpg", "H_11727.jpg", "H_11728.jpg", "H_11729.jpg", "H_11730.jpg", "H_11731.jpg", "H_11732.jpg", "H_11733.jpg", "H_11734.jpg", "H_11735.jpg", "H_11736.jpg", "H_11737.jpg", "H_11738.jpg", "H_11739.jpg", "H_11740.jpg", "H_11741.jpg", "H_11742.jpg", "H_11743.jpg", "H_11744.jpg", "H_11745.jpg", "H_11746.jpg", "H_11747.jpg", "H_11748.jpg", "H_11749.jpg", "H_11750.jpg", "H_11751.jpg", "H_11752.jpg", "H_11753.jpg", "H_11754.jpg", "H_11755.jpg", "H_11756.jpg", "H_11757.jpg", "H_11758.jpg"])

def move(filepath,filepath2,out=True):
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
            # Reverting commands:
            # print('"'+filepath2+'"', '"'+filepath+'"')
            if(out):print(filepath2, '\t',filepath)
    else:
        if(out):print('File already moved!', filepath2, filepath)
        # exit(0)

for sq in ['HQ','SQ','LQ']:
    for sl in ['HE','JE']:#,'HH','JH']:
        _dir = filtered_dir+"convertedOMRs_"+sq+"/"+sl+"/"
        if(not os.path.exists(_dir)):
            print('Created : '+ _dir)
            os.makedirs(_dir)

allOMRs= list(glob.iglob(dir_glob))
print("Total",len(allOMRs))

for filepath in allOMRs:
    # J_02777.jpg
    finder = re.search(r'outputs/CheckedOMRs/(.*)/convertedOMRs_LQ_(.*_.*)',filepath,re.IGNORECASE)
    if(finder):
        squadlang = finder.group(1)+"/"
        filename = finder.group(2)
        if(filename in GENUINES or filename in MOTHER_OF_GODS):
            print("skipped:",filename)
            continue
        counter += 1
        for sq in ['HQ','SQ','LQ']:
            folder_sub = 'convertedOMRs_' + sq +'/'
            inputpath = inputs_dir +folder_sub+squadlang+filename
            renamedpath =  filtered_dir +folder_sub + squadlang + squadlang[0] + "_" + format(counter,"0d") + ".jpg";
            # move from inputs to filtered with a rename
            move(inputpath, renamedpath, sq=='LQ')
    else:
        print("Unexpected filepath", filepath)
        exit(0)

print("\n\n\t\tSeparating MOG Counter:", counter,"\n\n")

# Put Genuines at the end
for filepath in allOMRs:
    # J_02777.jpg
    finder = re.search(r'outputs/CheckedOMRs/(.*)/convertedOMRs_LQ_(.*_.*)',filepath,re.IGNORECASE)
    if(finder):
        squadlang = finder.group(1)+"/"
        filename = finder.group(2)
        if not (filename in MOTHER_OF_GODS):
            continue
        counter += 1
        for sq in ['HQ','SQ','LQ']:
            folder_sub = 'convertedOMRs_' + sq +'/'
            inputpath = inputs_dir +folder_sub+squadlang+filename
            renamedpath =  filtered_dir +folder_sub + squadlang + squadlang[0] + "_" + format(counter,"0d") + ".jpg";
            # move from inputs to filtered with a rename
            move(inputpath, renamedpath, sq=='LQ')
    else:
        print("Unexpected filepath", filepath)
        exit(0)        

print("\n\n\t\tSeparating GEN Counter:", counter,"\n\n")

# Put Genuines at the end
for filepath in allOMRs:
    # J_02777.jpg
    finder = re.search(r'outputs/CheckedOMRs/(.*)/convertedOMRs_LQ_(.*_.*)',filepath,re.IGNORECASE)
    if(finder):
        squadlang = finder.group(1)+"/"
        filename = finder.group(2)
        if not (filename in GENUINES):
            continue
        counter += 1
        for sq in ['HQ','SQ','LQ']:
            folder_sub = 'convertedOMRs_' + sq +'/'
            inputpath = inputs_dir +folder_sub+squadlang+filename
            renamedpath =  filtered_dir +folder_sub + squadlang + squadlang[0] + "_" + format(counter,"0d") + ".jpg";
            # move from inputs to filtered with a rename
            move(inputpath, renamedpath, sq=='LQ')
    else:
        print("Unexpected filepath", filepath)
        exit(0)        

print("Total",len(allOMRs))
