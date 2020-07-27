#!/usr/bin/env python3
import random
from ascify.grid import AsciiGrid

size = (random.randint(1, 250), random.randint(1, 250))
step = random.randint(1, 8)
grid = AsciiGrid("./leader.jpg", step=step, size=size)
grid.start()
