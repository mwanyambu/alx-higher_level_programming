#!/usr/bin/python3
from sys import argv


def main():
    count = len(argv) - 1
    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(count))
    else:
        print("{} arguments:".format(count))
    for arg in range(1, count + 1):
        print("{}: {}".format(arg, argv[arg]))


if __name__ == "__main__":
    main()
