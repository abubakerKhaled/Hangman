import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words) # randomlly choose a word from the list of words
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman(words):
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has gussed

    lives = 6

    while len(word_letters) > 0 and lives > 0:

        # used letters
        print(f'You have {lives} lives left and You have used these letters: ', ' '.join(used_letters))

        # what current word is with - W - S
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        # getting the user input
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives-=1
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You have already guessed the letter. Please try again.')
        else:
            print('Invalid character. Please try again.')

    # gets here when the len(word_letters) == 0 OR lives == 0
    if lives == 0:
        print(f'You have lost, Sorry the word was {word}')
    else:
        print(f'You gussed the word {word}!!')


hangman(words)
