# Wordle Game

Welcome to the Wordle game! This is a simple word guessing game where you have to guess a five-letter word within a limited number of attempts.

## How to Play
1. Run the `wordle.py` file.
2. You will be prompted to guess the word. Enter your guess and press Enter.
3. The game will provide feedback on your guess:
   - A yellow tile (🟨) indicates that you selected the right letter but it's in the wrong spot.
   - A green tile (🟩) indicates the correct letter in the correct spot.
   - A grey tile (⬜) indicates the selected letter is not included in the target word.
4. Keep guessing until you either guess the word correctly or run out of attempts.

## Files
- `wordle.py`: Contains the main game code.
- `word-bank/all_words.txt`: A text file containing a list of all valid words.
- `word-bank/target_words.txt`: A text file containing a list of target words to be guessed in the game.

## How to Run
1. Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Clone or download this repository to your local machine.
3. Open a terminal or command prompt.
4. Navigate to the directory where you downloaded the repository.
5. Run the following command to start the game:
   ```sh
   python wordle.py
   ```
6. Follow the instructions provided in the console to play the game.

### Running Tests
To run the included doctests and ensure the game functions correctly, use the following command:
```sh
python wordle.py -t
```
This will execute the doctests and print the results. If all tests pass, you will see "Doctests passed!".

## Dependencies
- Python 3

## Troubleshooting
- Make sure the `word-bank` folder is in the same directory as `wordle.py`.

## Author
© 2024 Adrian Quayle

Enjoy playing Wordle!