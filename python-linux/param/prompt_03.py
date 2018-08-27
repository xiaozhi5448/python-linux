#!/usr/bin/env python
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

while True:
    user_input = prompt(u'>', history=FileHistory('history.txt'), auto_suggest=AutoSuggestFromHistory())
    print user_input
