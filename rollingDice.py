import random
from timeit import repeat


while repeat:
    print("your number is:", (random.randint(1,6)) )
    print("do you want to play again? yes or no:  ")
    repeat="yes".lower() in input()
   