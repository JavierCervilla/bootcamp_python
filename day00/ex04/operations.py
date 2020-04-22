#!/usr/bin/env python3

import sys
import math

def is_integer(num):
    try:
        int(num)
        return True
    except:
        usage()
        return False

def division_0(operation):
    print("ERROR (" + operation + " by zero)")
    exit(1)

def usage():
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("	python operations.py 10 3")
    exit(1)

def operation(num1, num2):
    print("%-20s %d" % ("sum:", num1 + num2))
    print("%-20s %d" % ("Difference:", num1 - num2))
    print("%-20s %d" % ("Product:", num1 * num2))
    try:
        print("%-20s %f" % ("Quotient:", num1 / num2))
        print("%-20s %d" % ("Remainder:", num1 % num2))
    except ZeroDivisionError:
        print("%-20s %s" % ("Quotient:", "ERROR (div by zero)"))
        print("%-20s %s" % ("Remainder:", "ERROR (modulo by zero)"))

def main():
    if len(sys.argv) != 3:
        usage()
    elif (is_integer(sys.argv[1]) == False and is_integer(sys.argv[2]) == False):
        usage()
    else:
        operation(int(sys.argv[1]), int(sys.argv[2]))
if __name__ == "__main__":
    main()
