import math
import random

from engine import play_game


def generate_lcm_question():
    numbers = [random.randint(1, 100) for _ in range(3)]
    question = " ".join(map(str, numbers))
    return question, math.lcm(*numbers)

if __name__ == "__main__":
    play_game(generate_lcm_question, "Find the smallest common multiple of given numbers.")
