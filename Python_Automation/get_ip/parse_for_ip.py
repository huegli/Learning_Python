#!/usr/bin/env python

import sys
import re

lines = sys.stdin.readlines()
# ip_line = lines[105]

id=0
while not ('IP Address' in lines[id]):
    id = id + 1

match = re.search('<td>(.+?)</td>', lines[id+1])
if match:
    print match.group(1)
