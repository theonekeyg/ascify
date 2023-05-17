#!/usr/bin/env python3
from ascify.grid import AsciiGrid
from ascify.renditions import truecolor_default

def main():
    grid = AsciiGrid("crab.png", step=5, size=(70, 120), rendition=truecolor_default)
    grid.start()
    print(grid)

if __name__ == "__main__":
    main()
