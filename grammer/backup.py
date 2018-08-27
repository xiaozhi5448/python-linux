import os
import Tkinter
import time


def backup():
    global source_entry
    global target_entry
    root_dir = '/home/xiaozhi/code/python/'
    today_dir = root_dir + time.strftime('%Y-%m-%d')
    target_file_name = time.strftime('%H:%M:%S') + '.zip'
    target_file_fallpath = today_dir + '/' + target_file_name

