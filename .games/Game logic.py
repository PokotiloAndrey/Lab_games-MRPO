import math
import random

def find_lcm(a, b, c):
    return math.lcm(a, b, c)

def play_lcm():
    print("Welcome to the Brain Games!\n")
    name = input("May I have your name? ")
    print(f"Hello, {name}!\nFind the smallest common multiple of given numbers.\n")

    for _ in range(3):
        numbers = [random.randint(1, 100) for _ in range(3)]
        correct_answer = find_lcm(*numbers)

        print(f"Question: {' '.join(map(str, numbers))}")
        user_answer = input("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!\n")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
