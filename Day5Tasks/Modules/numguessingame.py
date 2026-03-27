import random
import math
secret = random.randint(1,50)
attempts=5
for i in range(attempts):
    guess=int(input("Enter your guess (1-50):"))
    if guess == secret:
        print("Correct!,you guessed it.")
        break
    else:
        diff=math.fabs(secret-guess)
        print("Wrong guess!you are",diff,"away from the correct guess.")

if guess!=secret:
    print("!oops GAME OVER.The correct answer was",secret)