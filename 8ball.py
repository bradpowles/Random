import random

options = ["Yes", "No", "Try again", "Who knows", "Maybe"]

while True:
    enter = input("> ")
    print(random.choice(options))