#!/usr/bin/env python3

import string

def main():
	t = (19,42,21)
	l = len(t)
	str = "the {} numbers are: ".format(l)
	for i in t:
		if (l != 1):
			str += "{}, ".format(i)
			l -= 1
		else:
			str += "{}".format(i)
	print (str)

if __name__ == "__main__":
    main()
