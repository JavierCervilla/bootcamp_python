#!/usr/bin/env python3

import time
import os

def ft_progress(listy):
    strin = '>'
    start_time = time.time()
    for i in listy:
        percent =round(i / len(listy) * 100)
        if i % 50 == 0: strin = '=' + strin
        elapsed_time = round(time.time() - start_time, 2)
        print("ETA: {}[{:3}%][{}]{}/{}|elapsed time {}s".format(abs(round((elapsed_time * (i / len(listy)) - elapsed_time), 2)),percent, strin.ljust(21, " "), i, len(listy), elapsed_time))
        yield i


def main():
    iterations = 1000
    listy = range(iterations)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
        if elem < len(listy) - 1: os.system("clear")
    print(ret)

if __name__ == "__main__":
    main()
