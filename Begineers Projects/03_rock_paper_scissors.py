import random

# Emoji-enhanced choices
emoji_map = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

choices = list(emoji_map.keys())

while True:
    user_choice = input("Choose 🪨 Rock, 📄 Paper, or ✂️ Scissors (or type 'quit' to exit): ").lower()
    if user_choice == "quit":
        print("👋 Thanks for playing!")
        break
    if user_choice not in choices:
        print("❌ Invalid choice. Try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"🤖 Computer chose: {emoji_map[computer_choice]} {computer_choice.capitalize()}")

    # Determine the winner
    if user_choice == computer_choice:
        print("😐 It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")