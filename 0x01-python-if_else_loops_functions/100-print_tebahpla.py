#!/usr/bin/python3
r = 0
for c in range(122, 96, -1):
    print("{}".format(chr(c - r)), end="")
    r = 32 if r == 0 else 0
