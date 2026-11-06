# Name: Qingyun Li
# QCC ID: 24457146
import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

class DiceGame:
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()

    def evaluate_roll(self, total):
        if total in [7, 11]:
            return "Win"
        elif total in [2, 3, 12]:
            return "Lose"
        else:
            return "Roll Again"

    def play_round(self):
        d1 = self.die1.roll()
        d2 = self.die2.roll()
        total = d1 + d2
        result = self.evaluate_roll(total)
        return d1, d2, total, result

def main():
    game = DiceGame()
    while True:
        print("1. Play a round")
        print("2. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            d1, d2, total, result = game.play_round()
            print(f"Die 1: {d1}, Die 2: {d2}")
            print(f"Total: {total}")
            print(f"Result: {result}")
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()