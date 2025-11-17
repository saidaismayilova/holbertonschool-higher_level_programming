#!/usr/bin/python3
import sys
if _name_ == "_main_":
    argv=sys.argv[1:]
    total = 0
    for num in argv:
        total += int(num)
        print total
