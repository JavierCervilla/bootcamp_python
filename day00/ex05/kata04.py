def main():
    t = ( 0, 4, 132.42222, 10000, 12345.67)
    i = 0
    for j in t:
        i += 1
        if i == 1:
            if len(str(j)) == 1:
                day = "day_0{}".format(str(j))
            else:
                day = "day_".format(str(j))
        elif i == 2:
            if len(str(j)) == 1:
                ex = "ex_0{}".format(str(j))
            else:
                ex = "ex_{}".format(str(j))
        elif i == 3:
            f = "{0:.2f}".format(j)
        elif i == 4:
            nc1 = "{0:.2e}".format(j)
        else:
            nc2 = "{:.2e}".format(j)
    str1 = "{}, {} : {}, {}, {}".format(day, ex, f, nc1, nc2)
    print(str1)

if __name__ == "__main__":
    main()
