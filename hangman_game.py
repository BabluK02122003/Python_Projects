import random

words = ["CodeAlpha", "Python", "Programming", "Internship", "Hangman"]
word = random.choice(words)
guessed_letters = ["_"] * len(word)
max_incorrect_guesses = 6
incorrect_guesses = 0

print("Welcome to Hangman!")
print("You have", max_incorrect_guesses, "chances to guess the word.")

while True:
    print(" ".join(guessed_letters))
    guess = input("Guess a letter: ").lower()

    if guess in word.lower():
        for i in range(len(word)):
            if word[i].lower() == guess:
                guessed_letters[i] = word[i]
    else:
        incorrect_guesses += 1
        print("Incorrect! You have", max_incorrect_guesses - incorrect_guesses, "chances left.")

    if "_" not in guessed_letters:
        print("Congratulations! You won!")
        break
    elif incorrect_guesses == max_incorrect_guesses:
        print("Sorry, you lost. The word was", word)
        break
