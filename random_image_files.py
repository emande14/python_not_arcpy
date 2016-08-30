# Created 4/1/2016 by Edward Anderson
# Randomly copies a specified number of image files from the source directory and
# places them in the destination folder

import arcpy, random, shutil
arcpy.env.workspace = "C:\\temp\\2015\\"
files = arcpy.ListFiles()
img = []

for x in files:
    if x[-3:] == "jpg" or x[-3:] == "PNG":
        img.append(x)
    else:
        pass

for i in range(36): #specify the number of files to be copied, in this case 36 files
    y = random.randint(1,200) #this number should be equal to the number of files in the source folder
    src = "C:\\temp\\2015\\"+img[y] #source directory
    dst = "C:\\temp5\\"+img[y] #destination directory
    shutil.copy(src, dst)
    print img[y] #prints the files that were copied
