#this is guess the number game using the python library random
import random
n = random.randint(1, 30)


print("---------------------------------------------------")
print("|********WELCOME TO GUESS THE NUMBER GAME!********|")
print("---------------------------------------------------")
name=input("Whats your name?\n")
print("Okay %s lets play!" %(name))

guess = int(input("Enter an integer between 1 and 30: "))
while n != "guess":
    
    if guess < n:
        print("Your guess is low")
        guess = int(input("Enter an integer from 1 to 30: "))
    elif guess > n:
        print("Your guess is high")
        guess = int(input("Enter an integer from 1 to 30: "))
    else:
        print("Congratulations! You guessed it right!")
        break
    
