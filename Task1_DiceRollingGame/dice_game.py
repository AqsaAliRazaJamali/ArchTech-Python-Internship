import random


def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    print("\n Dice Results")
    print("-" * 25)
    print(f"Die 1 : {die1}")
    print(f"Die 2 : {die2}")
    print(f"Total : {die1 + die2}")
    print("-" * 25)


def main():
    print("=" * 40)
    print("      Dice Rolling Game")
    print("=" * 40)

    while True:
        roll_dice()

        choice = input("\nRoll again? (y/n): ").strip().lower()

        if choice in ['n', 'no']:
            print("\nThank you for playing!")
            break
        elif choice != 'y':
            print("Invalid input, but exiting anyway! Goodbye!")
            break


if __name__ == "__main__":
    main()
