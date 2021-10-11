
"""
def new_game():

    guesses = []
    correct_ans = 0
    question_num = 0

    for key in questions:
        print("-------------------------------")
        print(key)
        for i in options[question_num]:
            print(i)
        question_num += question_num
        if question_num ==3:
            break
        ans = input("Enter A, B, C or D")
        guesses.append(ans)
        correct_ans += check_answer(questions.get(key), ans)

        display_score(correct_ans)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0


def display_score(answer):
    print("Your total score is :" + answer)

def play_again():
    pass
"""
def new_game():

    question_number = 0
    guesses = []
    correct_ans = 0

    for key in questions:
        print("-----------------")
        print(key)
        for i in options[question_number]:
            print(i)
        question_number = question_number + 1
        if question_number ==5:
            break
        ans = input("Answer A, B, C or D : ")
        guesses.append(ans)
        correct_ans += check_answer(ans, questions.get(key))

    display_score(correct_ans, guesses, questions)



def check_answer(guess, answer):
    if guess == answer:
        print("Correct")
        return 1
    else:
        print("Hey its wrong and you suck")
        return 0


def display_score(correct_ans, guesses, questions):
    score = int((correct_ans/len(questions))*100)
    print("------------------")

    print("Your score is %s" ,score)



questions = {
    "Which is the most beautiful country?" : "A",
    "Which country has highest per capita income?" : "C",
    "Which is tech capital of India?" : "D",
    "Which country has the spiciest food?" : "B"
}

options = [["A. Iceland", "B. Switzerland", "C. India", "D. UK"],
 ["A. Luxemborg", "B. Monaco", "C. Qatar", "D. Switzerland"],
 ["A. Hyderabad", "B. Mumbai", "C. Delhi", "D. Banglore"],
 ["A. Italy", "B. India", "C. Mexico", "D. China"]]

new_game()
