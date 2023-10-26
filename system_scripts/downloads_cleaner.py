#!/usr/bin/python3
import os, time, stat


"""
Here is one of the First python scripts I created.
This script can be run as needed or set on a crontab. It prints our the file it deleted if its older that 2 weeks or passes over it.
"""

downloads_dir = r''

def file_age_in_seconds(pathname):
    return time.time() - os.stat(pathname)[stat.ST_MTIME]

for file in os.listdir(downloads_dir):
    file_path = '{}/{}'.format(downloads_dir,file)
    file_age = file_age_in_seconds(file_path)
    file_days = file_age // 86400
    if int(file_days) >= 14:
        try:
            os.remove(file_path)
            print('{} Deleted'.format(file))
        except:
            pass
    else:
        print('{} is not older than 2 weeks'.format(file))

