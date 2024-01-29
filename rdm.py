import random
import unittest

rdm = random.randint(1, 10)


def ran(ans, rand):
    if 0 < ans < 11:
        if rand == ans:
            print("You're a genius")
            return True
    else:
        print("I said enter a number between 1 and 10 maaaan")


if __name__ == "__main__":

    while True:
        try:
            answer = int(input("Guess a number between 1-10"))
            if ran(answer, rdm):
                break

        except ValueError:
            print("Please enter a number between 1-10")

