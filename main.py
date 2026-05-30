import random

secret_number=random.randint(1,100)

attempts=0

print("--NUMBER-GUESSING-GAME--")
print("I have chosen a number between 1 to 100.")

while True:
    guess=int(input("Enter your Guess: "))

    if guess<secret_number:
        print("Too LOW!!")
        attempts+=1
    elif guess>secret_number:
        print("Too HIGH!!")
        attempts+=1
    
    else:
        print(f"\nCongrats!!")
        print(f"You Guessed the number is {attempts} attempts.")
        break


    