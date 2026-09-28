import random
words = ["python", "technology", "program", "coding", "developer"]
word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6
print("================================")
print("       WELCOME TO HANGMAN")
print("================================")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")
# Main game loop
while incorrect_guesses < max_guesses:

    # Display the word with blanks
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the complete word has been guessed
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations! You guessed the word!")
        print("The word was:", word)
        break

    # Get user's guess
    guess = input("Enter a letter: ").lower()

    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the letter to guessed letters
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")
        print("Incorrect guesses:", incorrect_guesses, "/", max_guesses)

else:
    print("\n Game Over!")
    print("The correct word was:", word)
