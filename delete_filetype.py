# This script iterates through all folders in a specified directory, deleting
# a specified file type (in this case, .ovr files).
# For this script to work correctly, it should be saved in the same directory
# as the folders through which this script will iterate.

import os
pattern = '.ovr'

# Return all files in dir, and all its subdirectories, ending in pattern
def gen_files(dir, pattern):
   for dirname, subdirs, files in os.walk(dir):
      for f in files:
         if f.endswith(pattern):
            yield os.path.join(dirname, f)


# Remove all files in the current dir matching *.ovr
for f in gen_files('.', '.ovr'):
   os.remove(f)
   print f + " REMOVED"
