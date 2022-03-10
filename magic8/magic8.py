# Imports a random number generator
import random

# Sets up variables for the Magic 8 Ball
name = "Stevie"
question = "Should I have a job?"
answer = ""

# Generates a random number between 1 and 9
random_number = random.randint(1,9)

#print(random_number)

#Generates answers for each randomly generated value
if random_number == 1:
    answer = "Yes - definitely."
elif random_number == 2:
    answer = "It is decidedly so."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."
else:
    answer = "Error"

#Prints name, question, and answer.
if name == "":
  print("You ask: " + question + " Magic 8-Ball's answer: " + answer)
elif question == "":
  print(name + ", the Magic 8-Ball cannot provide a fortune unless you ask it something.")
else:
  print(name + " asks: " + question + " Magic 8-Ball's answer: " + answer)