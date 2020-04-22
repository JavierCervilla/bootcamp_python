#!/usr/bin/env python3

def main():
	phrase = "The right format"
	l = len(phrase)
	str = "{:{fill}{allign}{width}}".format(phrase, fill = "-", allign = '>', width = 42)
	print(str)

if __name__ == "__main__":
    main()
