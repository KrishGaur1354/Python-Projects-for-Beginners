def new_game():

    answers = []
    correct_answers = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        answers.append(guess)

        correct_answers += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_answers, answers)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_answers, answers):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Your answers: ", end="")
    for i in answers:
        print(i, end=" ")
    print()

    score = int((correct_answers/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "What is the difference between tuples and lists?: ": "C",
 "Which of these is not a mutable built-in type Python? : ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Tuples are enclosed with brackets while lists are not", "B. Tuples are bullet points while lists are numbers", "C. Tuples are enclosed within parentheses while list are not.", "D.Tuples are in Roman figures while lists are alphabetical"],
          ["A. Sets","B. Lists", "C. Tuples", "D. Dictionary"]]

new_game()

while play_again():
    new_game()

print("Byeeeeee!")