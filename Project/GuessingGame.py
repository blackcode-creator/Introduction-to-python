
# We are going to build a guessing game using a while loop
# Best practice is to write code in form of a story for easy readability

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
   guess = int(input('Guess: '))
   guess_count += 1
   if guess == secret_number:
       print("You Won")
       break
else:
    print('Sorry you failed')