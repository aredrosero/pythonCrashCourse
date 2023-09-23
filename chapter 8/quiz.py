
from choose import choice
A=1
B=3
C=2

selec = int((input("please choose the correct answer,'A, B or C': ")))

choice(selec)
print("Welcome to the quiz!")

# Define your questions and answer choices as dictionaries
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A. Paris", "B. Berlin", "C. London", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "What is the largest organ in the human body?",
        "choices": ["A. Heart", "B. Liver", "C. Brain", "D. Skin"],
        "answer": "D"
    },
    {
        "question": "What is the highest mountain in the world?",
        "choices": ["A. Kilimanjaro", "B. Mount Everest", "C. Mount Fuji", "D. Mount McKinley"],
        "answer": "B"
    }
]

score = 0

# Loop through each question and prompt the user to answer
for q in questions:
    print(q["question"])
    for c in q["choices"]:
        print(c)
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()
    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

# Display the user's score
print("You got", score, "out of", len(questions), "questions correct.")

questions = {
    "What is the capital of France?": ["A. Paris", "B. Berlin", "C. London"],
    "What is the largest ocean in the world?": ["A. Atlantic", "B. Indian", "C. Pacific"],
    "What is the highest mountain in the world?": ["A. K2", "B. Everest", "C. Kilimanjaro"]
}

# iterate over the questions and present them to the user
for question, answers in questions.items():
    print(question)
    for answer in answers:
        print(answer)
    
    # get the user's answer and check if it's correct
    user_answer = input("Enter your answer (A, B, or C): ")
    if user_answer.lower() == "a":
        print("Correct!")
    else:
        print("Incorrect.")

# define quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Madrid", "Berlin"],
        "answer": "Paris"
    },
    {
        "question": "Which is the largest country in the world by land area?",
        "options": ["Russia", "China", "USA", "Canada"],
        "answer": "Russia"
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Dollar", "Euro", "Yen", "Pound"],
        "answer": "Yen"
    }
]

# define function to display a question and its options
def display_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")

# define function to get the user's answer to a question
def get_user_answer():
    user_answer = input("Enter your answer (1-4): ")
    while user_answer not in ["1", "2", "3", "4"]:
        user_answer = input("Invalid answer. Please enter a number from 1 to 4: ")
    return user_answer

# define function to check if the user's answer is correct
def check_answer(question, user_answer):
    return question["options"][int(user_answer)-1] == question["answer"]

# define function to run the quiz
def run_quiz(questions):
    score = 0
    for question in questions:
        display_question(question)
        user_answer = get_user_answer()
        if check_answer(question, user_answer):
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
    print(f"You scored {score} out of {len(questions)}.")

# run the quiz
run_quiz(questions)        