# created 8/10/2016 by Eddie Anderson
# input: a directory containing folders to be zipped 
#      In the below script, all folders under C:\test will be individually zipped
# output: zipped folders
# NOTE: as currently written, this script will only correctly work if it is saved in the same
#      directory as the folders to be zipped.

import zipfile, os

for dirpath, folders, files in os.walk('C:\\test'):
    for folder in folders:
        print folder
        newZip = zipfile.ZipFile(folder+'.zip', 'w')
        for dirpath2, folders2, files2 in os.walk(folder):
            for f in files2:
                fn = os.path.join(dirpath2, f)
                newZip.write(fn, compress_type=zipfile.ZIP_DEFLATED)
                print str(fn) + " created"
        newZip.close()
        print str(folder) + " zipped"
