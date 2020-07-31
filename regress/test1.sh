#!/usr/bin/bash

tempfile=../test1.py
cat << EOF >$tempfile
from sys import argv
from ascify.grid import AsciiGrid
from ascify.renditions import default_rendition

grid = AsciiGrid("./leader.jpg", size=(60, 120), rendition=default_rendition)
grid.start()
with open("./60-120-grey", "r") as f:
    assert str(grid) == f.read(), "Failed %s test" % argv[0]
print("%s passed." % argv[0])
EOF

/usr/bin/env python3 $tempfile

rm $tempfile -f
