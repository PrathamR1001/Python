import random

# Number guessing game

LOWER = 1
UPPER = 100
DIFFICULTIES = {"easy": 10, "hard": 5}


def ask_difficulty():
    """Ask for a difficulty until a valid one is given, return the attempt count."""
    while True:
        choice = input("Choose difficulty: easy or hard: ").strip().lower()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print("Invalid difficulty. Please type 'easy' or 'hard'.")


def ask_guess():
    """Ask for a guess until it is a number inside the range, then return it."""
    while True:
        answer = input(f"Enter a number between {LOWER} and {UPPER}: ").strip()
        try:
            guess = int(answer)
        except ValueError:
            print("That's not a whole number. Try again.")
            continue

        if LOWER <= guess <= UPPER:
            return guess
        print(f"Out of range. Stay between {LOWER} and {UPPER}.")


def play_round():
    secret = random.randint(LOWER, UPPER)
    attempts_remaining = ask_difficulty()

    while attempts_remaining > 0:
        guess = ask_guess()
        attempts_remaining -= 1

        if guess == secret:
            print(f"You guessed it! The answer is {secret}")
            return

        hint = "Too High" if guess > secret else "Too Low"
        if attempts_remaining:
            print(f"{hint}. Attempts Remaining: {attempts_remaining}\n")
        else:
            print(hint)

    print(f"You ran out of attempts! The number was {secret}")


def main():
    print("Welcome to the number guessing game !!\n")
    while True:
        play_round()
        if input("\nPlay again? (y/n): ").strip().lower() not in ("y", "yes"):
            print("Thanks for playing!")
            return


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGame cancelled. Bye!")
