def play_game(game_logic, game_description):
    print("Welcome to the Brain Games!\n")
    name = input("May I have your name? ")
    print(f"Hello, {name}!\n{game_description}\n")

    for _ in range(3):
        question, correct_answer = game_logic()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!\n")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
