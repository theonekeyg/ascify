#!/usr/bin/env python3
from ascify.grid import AsciiGrid

def main():
    grid = AsciiGrid("leader.jpg", step=5, size=(70, 120))
    grid.start()
    print(grid)

if __name__ == "__main__":
    main()
