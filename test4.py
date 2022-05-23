import random

print("this will test you on your knowledge of maori numbers.\n"
      "you will need to enter the right maori word for each number.\n")

# checks your name
print("whats your name?: ")

name = input()


# list 1
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
# list 2
words = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]

question = random.choice(numbers)
attempt = input(f"what is the maori word for this number {name}? {question}: ")

# part of the code
answer_index = numbers.index(question)
answer = words[answer_index]

# checks if you have the right answer
if attempt == answer:
    print("correct")

else:
    print("incorrect")
