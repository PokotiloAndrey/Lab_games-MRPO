import random

from engine import play_game


def generate_progression_question():
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    progression = [start * (ratio ** i) for i in range(length)]
    
    hidden_index = random.randint(1, length - 2)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."

    question = " ".join(map(str, progression))
    return question, correct_answer

if __name__ == "__main__":
    play_game(generate_progression_question, "What number is missing in the progression?")
