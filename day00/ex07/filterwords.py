#!/usr/bin/env python3

import sys
import string
import re


def error():
    print("ERROR")
    exit(1)


def main():
    if len(sys.argv) == 3:
        try:
            num_letras = int(sys.argv[2])
        except:
            error()
        if sys.argv[1].isnumeric(): error()
        lista = [word for word in re.sub('[%s]' % re.escape(
            string.punctuation), '', sys.argv[1]).split(" ") if len(word) > num_letras]
        print(lista)
    else:
        error()


if __name__ == "__main__":
    main()
