#!/usr/bin/python3
print("{}".format(
    ", ".join("{:d} = 0x{:x}".format(i, i) for i in range(0, 99))
))
