import random
from questions import questions   # Import questions from Member 1's file


def shuffle_questions(q_list):
    """Shuffle questions so the quiz is different each time."""
    shuffled = q_list.copy()
    random.shuffle(shuffled)
    return shuffled


def ask_question(question_data, question_number):
    """Display one question and get the user's answer."""
    print(f"\nQ{question_number}: {question_data['question']}")
    print("-" * 50)

    for option in question_data["options"]:
        print(option)

    print()
    while True:
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer in ["A", "B", "C", "D"]:
            return user_answer
        else:
            print("❌ Invalid input! Please enter A, B, C, or D.")


def check_answer(user_answer, correct_answer):
    """Check if the user's answer is correct."""
    if user_answer == correct_answer:
        print("✅ Correct!")
        return True
    else:
        print(f"❌ Wrong! The correct answer was: {correct_answer}")
        return False


def run_quiz(player_name, num_questions=5):
    """Run the full quiz and return the final score."""
    print(f"\n🎯 Starting Quiz for: {player_name}")
    print("=" * 50)

    selected_questions = shuffle_questions(questions)[:num_questions]

    score = 0
    total = len(selected_questions)

    for i, q in enumerate(selected_questions, start=1):
        user_answer = ask_question(q, i)
        is_correct = check_answer(user_answer, q["answer"])

        if is_correct:
            score += 1

    return score, total