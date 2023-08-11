#!/usr/bin/python3
import sys


def main():
    i = sys.argv[1:]
    sum_total = sum(int(j) for j in i)
    print(sum_total)


if __name__ == "__main__":
    main()
