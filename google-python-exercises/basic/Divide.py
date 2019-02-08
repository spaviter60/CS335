#!/usr/bin/python -tt
import os

for i in [11, 9, 7, 2, 0]:
    try:
        print "The magic number is: %d" %(100/i)
    except ZeroDivisionError:
        print "The program is no Good"