#!/usr/bin/env python3
# Author: Mark Jordan Ndolla Wafo
# Author ID: mjndolla-wafo
# Date Created: 2026/01/20

import sys

if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer -= 1

print("blast off!")

