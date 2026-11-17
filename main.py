
from quiz_engine import run_quiz   # Import quiz engine from Member 2's file


# ---------- Leaderboard (stored as a list of dicts) ----------
leaderboard = []


def display_welcome():
    """Show a welcome banner."""
    print("=" * 50)
    print("   🐍 PYTHON QUIZ APPLICATION 🐍")
    print("   Test Your Python Knowledge!")
    print("=" * 50)


def get_player_name():
    """Ask for the player's name."""
    name = input("\nEnter your name: ").strip()
    if name == "":
        name = "Anonymous"
    return name


def show_result(player_name, score, total):
    """Show the player's score and grade."""
    percentage = (score / total) * 100

    print("\n" + "=" * 50)
    print(f"   📊 RESULTS FOR: {player_name.upper()}")
    print("=" * 50)
    print(f"   Score     : {score} / {total}")
    print(f"   Percentage: {percentage:.1f}%")

    # Give a grade based on score
    if percentage == 100:
        grade = "🏆 Perfect Score! Outstanding!"
    elif percentage >= 80:
        grade = "🥇 Excellent!"
    elif percentage >= 60:
        grade = "🥈 Good Job!"
    elif percentage >= 40:
        grade = "🥉 Keep Practicing!"
    else:
        grade = "📚 Study More Python!"

    print(f"   Grade     : {grade}")
    print("=" * 50)

    return percentage


def add_to_leaderboard(player_name, score, total, percentage):
    """Add the player's result to the leaderboard."""
    leaderboard.append({
        "name": player_name,
        "score": score,
        "total": total,
        "percentage": percentage
    })


def show_leaderboard():
    """Display the leaderboard sorted by score."""
    if not leaderboard:
        print("\n📋 No scores yet!")
        return

    # Sort by percentage (highest first)
    sorted_board = sorted(leaderboard, key=lambda x: x["percentage"], reverse=True)

    print("\n" + "=" * 50)
    print("        🏅 LEADERBOARD 🏅")
    print("=" * 50)
    print(f"{'Rank':<6} {'Name':<15} {'Score':<10} {'Percentage'}")
    print("-" * 50)

    for rank, entry in enumerate(sorted_board, start=1):
        print(f"{rank:<6} {entry['name']:<15} {entry['score']}/{entry['total']:<8} {entry['percentage']:.1f}%")

    print("=" * 50)


def ask_num_questions():
    """Ask how many questions the player wants."""
    print("\nHow many questions do you want?")
    print("  1) 5 Questions")
    print("  2) 8 Questions")
    print("  3) 10 Questions (All)")

    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        return 5
    elif choice == "2":
        return 8
    else:
        return 10


def main():
    """Main function — controls the whole app."""
    display_welcome()

    while True:
        print("\n📌 MAIN MENU")
        print("  1) Start Quiz")
        print("  2) View Leaderboard")
        print("  3) Exit")

        choice = input("\nEnter your choice (1/2/3): ").strip()

        if choice == "1":
            player_name = get_player_name()
            num_q = ask_num_questions()

            # Run the quiz (from Member 2's module)
            score, total = run_quiz(player_name, num_q)

            # Show results (Member 3's job)
            percentage = show_result(player_name, score, total)

            # Save to leaderboard
            add_to_leaderboard(player_name, score, total, percentage)

        elif choice == "2":
            show_leaderboard()

        elif choice == "3":
            print("\n👋 Thanks for playing! Keep learning Python! 🐍")
            break

        else:
            print("⚠️ Invalid choice! Please enter 1, 2, or 3.")


# ---------- Run the App ----------
if __name__ == "__main__":
    main()