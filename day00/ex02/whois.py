#!/usr/bin/env python3

import sys

def is_integer(num):
    try:
        int(num)
        return True
    except:
        error()
        return False

def error():
    print("ERROR")
    exit(1)

if len(sys.argv) == 2 and is_integer(sys.argv[1]):
    if (int(sys.argv[1]) == 0): print("I`m Zero")
    elif (int(sys.argv[1]) % 2 == 0): print("I`m Even")
    else: print("I`m Odd")
elif len(sys.argv) == 1: exit(1)
else: error()
