# zainab hasanzai

print("Welcome to quize game")
print()

questions = {
    "Question1: \n What's the capital of France?": {
        "options": ["a) Rome", "b) Berlin", "c) Paris", "d) Madrid"],
        "answer": "c"
    },
    "Question2: \n What's the most popular programming language?": {
        "options": ["a) Javascript", "b) Python", "c) Java", "d) C#"],
        "answer": "b"
    },
    "Question3: \n Who created the Python programming language?": {
        "options": ["a) Dennis Ritchie", "b) James Gosling", "c) Guido van Rossum", "d) None"],
        "answer": "c"
    },
    "Question4 \n Which of the following is not a programming language?": {
        "options": ["a) Python", "b) Java", "c) C++", "d) HTML"],
        "answer": "d"
    },
    "Question5 \n Which of the following data types in Python can store multiple values at ones?": {
        "options": ["a) int", "b) float", "c) list", "d) variables"],
        "answer": "c"
    }
}
score = 0
for q in questions:
    print(q)
    for option in questions[q]["options"]:
        print(option)
    user = input("Your answer: ")
    if user.lower() == questions[q]["answer"]:
        print("correct")
        score += 1
    else:
        print("wrong")

print("Game finished!")
print("Your score is: ", score)