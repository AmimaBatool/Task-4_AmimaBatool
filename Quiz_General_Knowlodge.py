#=======THE GENERAL KNOWLEDGE QUIZ GAME==========

questions = ("How many continents are there in the world?, ",
            "Who is known as the father of computers? ",
            "What is the Chemical Symbol for Water? ",
            "Which is the largest planet in our solar system? ",
            "Which language is primarily used to create the structure of web pages? ",
            "Which is the fastest land animal? ",
            "What is the capital of France? ",
            "How many players are there in a football team? ",
            "How many bones are there in the human body? ",
            "Which planet is the hottest in our solar system? "
           )

options = ( ("A) 5", "B) 6", "C) 7", "D) 8" ),
            ("A) Alan Turing", "B) Charles Babbage", "C) John von Neumann", "D) Bill Gates" ),
            ("A) H2O", "B) CO2", "C) NaCl", "D) O2" ),
            ("A) Jupiter", "B) Saturn", "C) Uranus", "D) Neptune" ),
            ("A) JavaScript", "B) Python", "C) HTML", "D) CSS" ),
            ("A) Cheetah", "B) Lion", "C) Horse", "D) Dog" ),
            ("A) London", "B) Berlin", "C) Paris", "D) Rome" ),
            ("A) 10", "B) 11", "C) 12", "D) 13" ),
            ("A) 206", "B) 205", "C) 201", "D) 208" ),
            ("A) Venus", "B) Mercury", "C) Mars", "D) Jupiter" )
          )

answers = ("C", "B", "A", "A", "C", "A", "C", "C", "A", "B")
guesses = []
score = 0
question_number = 0

print("----------------------------")
print("General Knowledge Quiz Game")
print("----------------------------")

for question in questions:
    print("----------------------------")
    print(question)
    for option in options[question_number]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_number]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
        print(f"{answers[question_number]} is the correct answer.")

    question_number += 1


print()
print("Quiz completed!")
print()
print("------YOUR RESULT------")
print()

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Your guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

print(f"Total Correct answers: {score}")

percentage = score/ len(questions) * 100
print(f"Your percentage is: {percentage}%")
print()