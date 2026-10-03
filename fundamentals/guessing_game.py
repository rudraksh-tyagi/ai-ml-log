word = "python"
guess = ""
guess_count = 0
out_of_guesses = False
while(word != guess and not out_of_guesses):
    guess = input("Enter a guess: ")
    guess_count += 1
    if(guess == word):
        print("You guessed the word in " + str(guess_count) + " tries!")
        break
    if(guess_count >= 3):
        out_of_guesses = True
if(out_of_guesses):
    print("You are out of guesses. The word was: " + word)

    