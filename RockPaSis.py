import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]

    while True:
        user = input("Enter rock/paper/scissors (or quit): ").lower()
        if user == "quit":
            print("👋 Goodbye!")
            break
        if user not in choices:
            print("⚠ Invalid choice.")
            continue

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        if user == computer:
            print("It's a draw!")
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            print("🎉 You win!")
        else:
            print("💻 Computer wins!")

if __name__ == "__main__":
    rock_paper_scissors()
