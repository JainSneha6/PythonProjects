from random import randint

num=randint(1,101)

print("Welcome to Guessing Game!")
print("Rules: ")
print("I am thinking of a number between 0 and 100")
print("COLD - If your guess is more than 10 away from my number")
print("WARM - If your guess within 10 of my number")
print("COLDER - If your guess is farther than your recent guess")
print("WARMER - If your guess is closer than your recent guess")
print("LET'S PLAY")

guess=[]

while True:
    user_input=int(input("What is your guess? "))
    
    if user_input<1 or user_input>100:
        print("OUT OF BOUNDS! Try again: ")
        continue
    
    if user_input==num:
        print("Congratulations!")
        print(f"You've guessed {num} in {len(guess)} Guesses!")
        break
    
    guess.append(user_input)
    
    if len(guess)==1:
        if abs(user_input-num)<=10:
            print("WARM!")
        else:
            print("COLD!")
    else:
        if abs(user_input-num)<=abs(num-guess[-2]):
            print("WARMER!")
        else:
            print("COLDER!")