#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import fnmatch


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
