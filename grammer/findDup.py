from __future__ import print_function
import hashlib
import fnmatch
import os
import sys


CHUNK_SIZE = 8192

def is_file_match(filename, partterns):
    for parttern in partterns:
        if fnmatch.fnmatch(filename, parttern):
            return True
        else:
            return False


def find_specific_file(root, partterns=['*'], exclude_dir=[]):
    for rootdir, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if is_file_match(filename, partterns):
                yield os.path.join(rootdir, filename)

        for dirname in dirnames:
            if dirname in exclude_dir:
                dirnames.remove(dirname)

def get_chunk(filename):
    with open(filename) as f:
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            else:
                yield chunk

def get_chsum(filename):
    d = hashlib.md5()
    for chunk in get_chunk(filename):
        d.update(chunk)
    return d.hexdigest()

def main():
    sys.argv.append("")
    if not os.path.isdir(sys.argv[1]):
        print("{0} is not dir!".format(sys.argv[1]))
        exit()
    record = {}
    for item in find_specific_file(sys.argv[1]):
        checkres = get_chsum(item)
        if checkres in record:
            print("find duplicate file {0} vs {1}".format(record[checkres], item))
        else:
            record[checkres] = item

    print("filelist:",record)

if __name__ == '__main__':
    main()



