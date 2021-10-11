import random

gen_num = random.randint(0,100)
print("Welcome to the guess the number game")
print("---------------------")
while True:
    guess = int(input("Guess any number between 1 and 100 : "))
    if guess == gen_num:
        print("Wow you are genius you gave corrct answer")
        break
    elif guess > gen_num:
        print("Your guess is high")
    else:
        print("Your guess is too low")


