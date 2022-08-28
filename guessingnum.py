import random

numbers = random.randint(0,100)
attempts = 0
while True:
    try:
        guess = int(input("Enter your Guess: "))

        if numbers == guess:
            attempts = attempts + 1
            print(' Guess in {attempts} attempts. ')
            break
        elif numbers > guess:
            print("Enter a Higher Number")
            attempts = attempts + 1
        else:
            print("Enter a Lower Number")
            attempts = attempts + 1

    except:
            print("Choose No. between 1 to 100 ")
