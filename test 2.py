# this is a quiz that tests your knowledge on the maori numbers from 1-10
from random import randint

print("This is a small quiz that will test how well you know maori numbers from 1-10")
print("This is simple all you have to do is type in your name and start answering")
print("You will be graded at the end of the quiz")
print(""
      ""
      ""
      "")
print("whats your name?:  ")

name = input()

print(f"the quiz is about to begin {name}! ")


for _ in range(10):
    value = randint(1, 10)

    print(value)


print(f"what is that in maori {name}?: ")

if 1 == "tahi":
    print("correct")

