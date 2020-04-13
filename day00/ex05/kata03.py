#!/usr/bin/env python3

def main():
	phrase = "The right format"
	l = len(phrase)
	str = "{}{}".format((42 - len(phrase)) * "-", phrase)
	print(str)

if __name__ == "__main__":
    main()
