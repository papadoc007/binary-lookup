import random

print("Welcome to the Game!")
secret = random.randint(1, 1000000)
print(secret)

attempts = int(input("Enter number of attempts: "))
low = 1
high = 1000000

while attempts > 0:
    print(f"You have {attempts} attempts left.")
    guess = (low + high) // 2
    print(f"Guessing {guess}")
    if guess == secret:
        print("Congratulations! You guessed the secret number!")
        break
    elif guess < secret:
        print("Too low")
        low = guess + 1
    else:
        print("Too high")
        high = guess - 1
    attempts -= 1

if attempts == 0:
    print("Sorry, you've run out of attempts. Better luck next time!")
