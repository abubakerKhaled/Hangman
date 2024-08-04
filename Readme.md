# Hangman Game

A simple command-line implementation of the classic Hangman game in Python.

## Description

This Hangman game randomly selects a word from a predefined list and allows the player to guess letters. The player has 6 lives, and with each incorrect guess, they lose a life. The game continues until the player guesses the word correctly or runs out of lives.

## Features

- Random word selection from a word list
- User-friendly command-line interface
- Displays used letters and current word progress
- Keeps track of remaining lives

## Requirements

- Python 3.x
- `words.py` file containing a list of words

## How to Run

1. Ensure you have Python installed on your system.
2. Place the `hangman.py` and `words.py` files in the same directory.
3. Run the game using the command:


## How to Play

1. The game will select a random word.
2. You will be prompted to guess a letter.
3. If the letter is in the word, it will be revealed in the word display.
4. If the letter is not in the word, you lose a life.
5. Keep guessing letters until you complete the word or run out of lives.

## Code Structure

- `get_valid_word(words)`: Selects a valid word from the word list.
- `hangman(words)`: Main game function that handles the game logic.

## Future Improvements

- Add difficulty levels
- Implement a graphical user interface
- Add a score system
- Expand the word list

## Contributing

Feel free to fork this project and submit pull requests with improvements or bug fixes.

## License

This project is open source and available under the [MIT License](LICENSE).