#!/usr/bin/env python3

def main():
    t = (3,30,2019,9,25)
    i = 0
    for j in t:
        i += 1
        if i == 1:
            if len(str(j)) == 1:
                hour = '0' + str(j)
            else:
                hour = str(j)
        elif i == 2:
            if len(str(j)) == 1:
                mins = '0' + str(j)
            else:
                mins = str(j)
        elif i == 3:
            age = str(j)
        elif i == 4:
            if len(str(j)) == 1:
                month = '0' + str(j)
            else:
                month = str(j)
        else:
            if len(str(j)) == 1:
                day = '0' + str(j)
            else:
                day = str(j)
    str1 = "{}/{}/{} {}:{}".format(month,day,age,hour,mins)
    print(str1)

if __name__ == "__main__":
    main()
