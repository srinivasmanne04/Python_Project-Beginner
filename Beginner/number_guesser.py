import random
top_range = input("Enter a number: ")
if top_range.isdigit():
    top_range = int(top_range)
    if top_range <= 0:
        print("Please enter a number greater than 0 next time.")
        quit()
else:
    print("Enter a valid number.")
    quit()

random_number = random.randint(0, top_range)
print(random_number)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Enter a valid number.")
        continue

    if user_guess == random_number:
        print("You got it right!")
        break
    elif user_guess > random_number:
        print("You were above the number.")
    else:
        print("You were below the number.")

print(f"You got it in {guesses} guesses.")