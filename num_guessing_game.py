import random as r

print("Welcome to Number Guessing Game !")
random_int = r.randint(1,10)
guess_num = 0 

while guess_num != random_int :
    guess_num = int(input("Guess the number (1-10) : "))
    if guess_num<random_int :
        print("Too Low!!!")
    elif guess_num>random_int :
        print("Too High!!!")
    else:
        print("Correct! You guessed the number!!!")