#!/usr/bin/bash

tempfile=../test3.py
cat << EOF >$tempfile
from sys import argv
from ascify.grid import AsciiGrid
from ascify.renditions import truecolor_default

grid = AsciiGrid("./leader.jpg", size=(60, 120), rendition=truecolor_default)
grid.start()
with open("./60-120-colored", "r") as f:
    assert str(grid) == f.read(), "Failed %s test" % argv[0]
print("%s passed." % argv[0])
EOF

/usr/bin/env python3 $tempfile

rm $tempfile -f
