#!/usr/bin/bash

tempfile=../test2.py
cat << EOF >$tempfile
import random
from sys import argv
from ascify.grid import AsciiGrid

size = (random.randint(1, 180), random.randint(1, 180))
step = random.randint(1, 6)
grid = AsciiGrid("./leader.jpg", step=step, size=size)
grid.start()
print("%s passed" % argv[0])
EOF

/usr/bin/env python3 $tempfile

rm $tempfile -f
