#!/usr/bin/env python3

import random



def new_number():
    return input("what is your guess?\n")


def main():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end game")
    secret_number = random.randint(1, 99)
    counter = 0
    while 1:
        counter += 1
        in_num = new_number()
        if in_num == 'exit':
            exit(1)
        try:
            num = int(in_num)
        except:
            print("That`s not a number.")
            num = 0
        if not num in range(1, 99):
            print("usage: number between 1 and 99")
        else:
            if num < secret_number:
                print("Too low!")
            elif num > secret_number:
                print("Too high!")
            elif num == secret_number:
                print("Congratulations. You got it")
                print("you won in {} attempts.".format(counter))
                if num == 42:
                    print(
                        "42\nThe answer to the ultimate question of life, the universe and everything is 42.")
                exit(0)
        num = 0


if __name__ == "__main__":
    main()
