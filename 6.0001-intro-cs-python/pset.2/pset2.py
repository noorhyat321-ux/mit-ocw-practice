# Part 1: Helper Functions
def is_word_guessed(secret_word, letters_guessed):
    return all(char in letters_guessed for char in secret_word)

def get_guessed_word(secret_word, letters_guessed):
    return "".join([char if char in letters_guessed else "_ " for char in secret_word])

def get_available_letters(letters_guessed):
    import string
    return "".join([c for c in string.ascii_lowercase if c not in letters_guessed])

# Part 2: Main Game Loop (Simplified Version)
def hangman(secret_word):
    guesses = 6
    letters_guessed = []
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    
    while guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
        print(f"Guesses left: {guesses}")
        guess = input("Please guess a letter: ").lower()
        
        if guess in letters_guessed:
            print("Oops! You've already guessed that.")
        elif guess in secret_word:
            letters_guessed.append(guess)
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(guess)
            guesses -= 2 if guess in 'aeiou' else 1
            print("Oops! That letter is not in my word.")
    
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)
