import random

print("this will test you on your knowledge of maori numbers.\n"
      "you will need to enter the right maori word for each number\n")
print("this small quiz will just ask you what some numbers are in maori.\n"
      "all you need to do is enter your name at the beginning and answer the questions.\n"
      "the test will continue once you enter your name\n")
# checks your name
print("whats your name?: ")

name = input()

score = 0
# list 1
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
# list 2
words = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]

question = random.choice(numbers)
attempt = input(f"what is the maori word for this number {name}? {question}: ")

# part of the code
answer_index = numbers.index(question)
answer = words[answer_index]

# checks if you have he right answer
if attempt == answer:
    print("correct")
    score = score + 1

else:
    print("incorrect")


question = random.choice(numbers)
attempt = input(f"what is the maori word for this number {name}? {question}: ")

# part of the code
answer_index = numbers.index(question)
answer = words[answer_index]

# checks if you have he right answer
if attempt == answer:
    print("correct")
    score = score + 1

else:
    print("incorrect")


question = random.choice(numbers)
attempt = input(f"what is the maori word for this number {name}? {question}: ")

# part of the code
answer_index = numbers.index(question)
answer = words[answer_index]

# checks if you have he right answer
if attempt == answer:
    print("correct")
    score = score + 1

else:
    print("incorrect")

question = random.choice(numbers)
attempt = input(f"what is the maori word for this number {name}? {question}: ")

# part of the code
answer_index = numbers.index(question)
answer = words[answer_index]

# checks if you have he right answer
if attempt == answer:
    print("correct")
    score = score + 1

else:
    print("incorrect")

question = random.choice(numbers)
attempt = input(f"what is the maori word for this number {name}? {question}: ")

# part of the code
answer_index = numbers.index(question)
answer = words[answer_index]

# checks if you have he right answer
if attempt == answer:
    print("correct")
    score = score + 1

else:
    print("incorrect")

question = random.choice(numbers)
attempt = input(f"what is the maori word for this number {name}? {question}: ")

# part of the code
answer_index = numbers.index(question)
answer = words[answer_index]

# checks if you have he right answer
if attempt == answer:
    print("correct")
    score = score + 1

else:
    print("incorrect")

question = random.choice(numbers)
attempt = input(f"what is the maori word for this number {name}? {question}: ")

# part of the code
answer_index = numbers.index(question)
answer = words[answer_index]

# checks if you have he right answer
if attempt == answer:
    print("correct")
    score = score + 1

else:
    print("incorrect")

question = random.choice(numbers)
attempt = input(f"what is the maori word for this number {name}? {question}: ")

# part of the code
answer_index = numbers.index(question)
answer = words[answer_index]

# checks if you have he right answer
if attempt == answer:
    print("correct")
    score = score + 1

else:
    print("incorrect")

question = random.choice(numbers)
attempt = input(f"what is the maori word for this number {name}? {question}: ")

# part of the code
answer_index = numbers.index(question)
answer = words[answer_index]

# checks if you have he right answer
if attempt == answer:
    print("correct")
    score = score + 1

else:
    print("incorrect")

question = random.choice(numbers)
attempt = input(f"what is the maori word for this number {name}? {question}: ")

# part of the code
answer_index = numbers.index(question)
answer = words[answer_index]

# checks if you have he right answer
if attempt == answer:
    print("correct")
    score = score + 1

else:
    print("incorrect")

# shows score
print(f"{name}'s score is")
print(score)
print("out")
print("of")
print("10")
print("thanks for doing this small quiz")
