import sys
import os
import hashlib

def md5(file_path):
    """ Return an md5 checksum for a file """
    read_file = open(file_path)
    the_hash = hashlib.md5()
    for line in read_file.readlines():
        the_hash.update(line)
    return the_hash.hexdigest()

def directory_listing(directory):
    """ return all of the files in a directory """
    dir_file_list = {}
    dir_root = None
    dir_trim = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        if dir_root is None:
            dir_root = dirpath
            dir_trim = len(dir_root)
            print("dir", directory)
            print("root is", dir_root)
        trimmed_path = dirpath[dir_trim:]
        if trimmed_path.startswith(os.sep):
            trimmed_path = trimmed_path[1:]
        for each_file in filenames:
            file_path = os.path.join(
                            trimmed_path, each_file)
            dir_file_list[file_path] = True
    return(dir_file_list, dir_root)

if len(sys.argv) < 3:
    print("You need to provide additional arguments")
    print(sys.argv[0], "<Directory 1>", "<Directory 2>")
    exit()

if len(sys.argv) > 3:
    print("Try using quotes in your path name")
    exit()

directory1 = sys.argv[1]
directory2 = sys.argv[2]

dir1_file_list, dir1_root = directory_listing(directory1)
dir2_file_list, dir2_root = directory_listing(directory2)

for file_path in dir2_file_list.keys():
    if file_path not in dir1_file_list:
        print(file_path, "Not found in directory 1")
    else:
        print(file_path, "Found in directory 1 and 2")
        file1 = os.path.join(dir1_root, file_path)
        file2 = os.path.join(dir2_root, file_path)
        if md5(file1) != md5(file2):
            print(file1, "and", file2, "differ")
        del dir1_file_list[file_path]
