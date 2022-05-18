# this is a quiz on maori numbers
# generates random number from 1-10
from random import randint

# checks your name
print("whats your name?: ")

name = input()

# asks if you have done this quiz before or not
print(f"have you done this quiz before {name}?: ")

while True:

    value = randint(1, 10)


    answer = input()
# if user says y the program continues
    if answer == "y":
        print("continuing to quiz...")
        print(value)
# if user says n show how the quiz works
    elif answer == "n":
        print("this is a quiz that will generate random numbers and you have to guess in maori")
        print(value)

# if user doesn't type y or n loop back
    else:
        if answer == "y":
            print(f"whats this number in maori {name}?:" )




