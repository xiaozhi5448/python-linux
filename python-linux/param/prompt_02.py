#!/usr/bin/env python
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory

while True:
    user_input = prompt(u'>', history=FileHistory('history.txt'))
    print user_input
