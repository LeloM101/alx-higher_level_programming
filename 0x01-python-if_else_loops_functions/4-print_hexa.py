#!/usr/bin/python3

''' print all numbers from 0 to 98'''

for i in range(0, 99):
    f = hex(i)
    print("{} = {}".format(i, f))
