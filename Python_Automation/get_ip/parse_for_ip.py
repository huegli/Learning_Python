#!/usr/bin/env python

import sys
import re

lines = sys.stdin.readlines()
ip_line = lines[105]

match = re.search('<td>(.+?)</td>', ip_line)
if match:
    print match.group(1)
