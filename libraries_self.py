import sys
import os
import hashlib

if len(sys.argv) < 3:
    print("You need to provide additional arguments")
    sys.exit

if len(sys.argv) > 3:
    print("Try using quotes in your path name")
    sys.exit

directory1 = sys.argv[1]
directory2 = sys.argv[2]

for dirpath, dirnames, filenames in os.walk(directory1):
    print("DIRPATH:", dirpath)
    print("---")
    print("DIRNAMES", dirnames)
    print("---")
    print("FILENAMES", filenames)
    print("---")
    sys.exit
