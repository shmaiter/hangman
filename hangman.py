import random
import string
from words import words


def get_valid_word(words):
    word = random.choice(words)

    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def start_hangman():
    random_word = get_valid_word(words)
    # print(random_word)
    word_letters = set(random_word)  # Sets don't allow repeated items.
    used_letters = set()
    alphabet = set(string.ascii_uppercase)

    lives = 8

    while len(word_letters) > 0 and lives > 0:

        # INFO ABOUT STATE
        print("\nUsed letters: ", ' '.join(used_letters))

        ordered_word = [
            letter if letter in used_letters else "-" for letter in random_word]
        print("\nCurrent word: ", ordered_word)

        user_letter = input("\nEnter a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("\nSorry! The letter is not part of the word.")

        elif user_letter in used_letters:
            print("\nYou've already used that letter.")

        else:
            print("\nThat's not a valid letter.")

    if lives == 0:
        print("\nYou lost!! The word was:", random_word)
    else:
        print("\nSuccess! You guessed the correct word:", random_word)


start_hangman()
