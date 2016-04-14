#!/usr/bin/env python

import sys
import re
import os
import time

# read in entire webpage as list of strings
lines = sys.stdin.readlines()

# find the index of line containing 'IP Address'
for id in range(len(lines)):
    if 'IP Address' in lines[id]:
        break

# actual IP address will be in the following line, use regex to extract
ipregex = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3})')
match = ipregex.search(lines[id+1])

# write result
if match:

    # first make sure we have proper file & directory
    logpath = os.path.join(
            os.path.expanduser('~'),
            'log')
    if not os.path.exists(logpath):
        os.makedirs(logpath)
    logname = os.path.join(logpath, 'external_ip.log')
    logfile = open(logname,'a')

    # write out date stamp and IP address
    logfile.write(time.strftime("%c"))
    logfile.write(' ' + match.group() + '\n')
    logfile.close

