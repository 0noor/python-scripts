import random
import sys
try:
    int(sys.argv[1])
    int(sys.argv[2])
except ValueError:
    print("please enter a number")
while True:
    try:
        num = int(input(f"Please choose a number between {str(int(sys.argv[1]))} and {str(int(sys.argv[2]))}: "))
        rand = random.randint(int(sys.argv[1]), int(sys.argv[2]))
        if num == rand:
            print("Your a genius")
            break
        elif num == 0:
            break
        else:
            print(f"Wrong!!! number was {rand} and you chose {num} ")
    except ValueError:
        print("Please enter an int")


