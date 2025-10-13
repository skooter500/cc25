import random

r = random.randrange(0, 10)
val = -1
while val != r:
    print(r)
    print("Guess the number I am thinking of:")
    val = int(input())

    if val == r:
        print("Correct!!")

    elif val > r:
        print("Too high")
    else:
        print("Too low")
