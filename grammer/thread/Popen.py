#!/usr/bin/env python
import subprocess
def popen_run(cmd):
    th = subprocess.Popen(cmd,
                         shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = th.communicate()
    if th.returncode != 0:
        return th.returncode, stderr
    return th.returncode, stdout
