from __future__ import print_function
import fileinput


for line in fileinput.input():
    meta = [fileinput.filename(), fileinput.fileno(), fileinput.filelineno(), fileinput.isstdin()]
    print(*meta, end="")
    print(line, end="")

