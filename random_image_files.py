#Created 4/1/2016 by Edward Anderson
#Randomly copies a random number of image files from the source directory and
#places them in the destiniation folder

import arcpy, random, shutil
arcpy.env.workspace = "C:\\temp\\internet\\2015\\"
files = arcpy.ListFiles()
img = []

for x in files:
    if x[-3:] == "jpg" or x[-3:] == "PNG":
        img.append(x)
    else:
        pass
#x = random.randint(1,6)

for i in range(36):
    y = random.randint(1,200)
    src = "C:\\temp\\internet\\2015\\"+img[y]
    dst = "C:\\temp5\\"+img[y]
    shutil.copy(src, dst)
    print img[y]
    del y, src, dst
