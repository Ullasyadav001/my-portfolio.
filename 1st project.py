import os

# Define the quiz questions using a list of dictionaries
QUESTIONS = [
    {
        "question": "What does HTML stand for?",
        "options": ["A. Hyper Text Markup Language", "B. High Tech Modern Language", "C. Hyperlink Text Management Language", "D. Home Tool Markup Language"],
        "answer": "A"
    },
    {
        "question": "Which programming language is known for its readability and simplicity?",
        "options": ["A. C++", "B. Java", "C. Python", "D. JavaScript"],
        "answer": "C"
    },
    {
        "question": "What is the correct file extension for a Python script?",
        "options": ["A. .pt", "B. .py", "C. .pyt", "D. .python"],
        "answer": "B"
    },
    {
        "question": "Which data structure holds key-value pairs in Python?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
        "answer": "D"
    },
    {
        "question": "What is the purpose of Git?",
        "options": ["A. Style websites", "B. Version control and tracking code changes", "C. Run database queries", "D. Compile Python code"],
        "answer": "B"
    }
]

FILENAME = "high_scores.txt"

def load_high_score():
    """Reads the current high score from the text file."""
    if not os.path.exists(FILENAME):
        return 0
    try:
        with open(FILENAME, "r") as file:
            content = file.read().strip()
            return int(content) if content.isdigit() else 0
    except IOError:
        return 0

def save_high_score(score):
    """Saves a new high score to the text file."""
    try:
        with open(FILENAME, "w") as file:
            file.write(str(score))
    except IOError:
        print("Error saving high score.")

def run_quiz():
    print("=" * 40)
    print("      🚀 WELCOME TO THE PYTHON QUIZ 🚀      ")
    print("=" * 40)
    
    high_score = load_high_score()
    print(f"Current High Score to beat: {high_score}\n")
    
    score = 0
    
    # Loop through the logic and list of questions
    for i, q in enumerate(QUESTIONS, 1):
        print(f"Question {i}: {q['question']}")
        for option in q['options']:
            print(option)
            
        # Input verification loop
        while True:
            choice = input("Your answer (A, B, C, or D): ").strip().upper()
            if choice in ['A', 'B', 'C', 'D']:
                break
            print("Invalid input. Please choose A, B, C, or D.")
            
        if choice == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.\n")
            
    print("=" * 40)
    print(f"🎉 Game Over! Your final score: {score}/{len(QUESTIONS)}")
    
    # Check for new high score
    if score > high_score:
        print(f"🌟 New High Score! You beat the old score of {high_score}!")
        save_high_score(score)
    else:
        print(f"Keep practicing to beat the high score of {high_score}!")
    print("=" * 40)

if __name__ == "__main__":
    run_quiz()