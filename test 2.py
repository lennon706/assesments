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

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

words = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]

for _ in range(1):
    value = random(1, 10)

    print(value)

question = random.choice(numbers)
attempt = input(f"what is the maori word for this number {name} {question}: ")

# part of the code
answer_index = numbers.index(question)
answer = words[answer_index]

# checks if you have he right answer
if attempt == answer:
    print("correct")

else:
    print("incorrect")



