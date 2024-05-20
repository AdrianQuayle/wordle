import random

ALL_WORDS = 'word-bank/all_words.txt'
TARGET_WORDS = 'word-bank/target_words.txt'

GUESSES = 6
WORD_LENGTH = 5

def welcome():
    print("""
+----------------------------------------------------------------------------------------------+     
|                                                                                              |
|    Welcome to Wordle!                                                                        |
|    You have 6 tries to guess the five-letter word.                                           |
|    Type your guess into the console and submit by pressing enter.                            |
|    A yellow tile indicated that you selected the right letter but it's in the wrong spot.    |
|    A green tile indicates the correct letter in the correct spot.                            |
|    A grey tile indicated the selected letter is not included in the target word.             |
|                                                                                              |
+----------------------------------------------------------------------------------------------+
    """)

def generate_list(file_path):
    file = open(file_path, 'r').read().splitlines()
    return file

def guess_input():
    while True:
        try:
            guess = str(input("Guess the word: ").lower())
            if len(guess) == WORD_LENGTH:
                if guess in valid_words:
                    print()
                    break
                else:
                    print("Invalid word\n")
            else:
                print("Input must be 5 characters long\n")
        except:
            print("Invalid input\n")
    return guess

def score_guess(guess, secret_word):
    """                                                       
    >>> score_guess('hello', 'hello')
    (2, 2, 2, 2, 2)
    >>> score_guess('drain', 'float')
    (0, 0, 1, 0, 0)
    >>> score_guess('hello', 'spams')
    (0, 0, 0, 0, 0)
    >>> score_guess('gauge', 'range')
    (0, 2, 0, 2, 2)
    >>> score_guess('melee', 'erect')
    (0, 1, 0, 1, 0)
    >>> score_guess('array', 'spray')
    (0, 0, 2, 2, 2)
    >>> score_guess('train', 'tenor')
    (2, 1, 0, 0, 1)
    """
    score = []
    word = list(secret_word)
        
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            score.append(2)
            word[i] = ''
        else:
            score.append(0)

    for i in range(len(guess)):
         if score[i] == 0 and guess[i] in word:
            score[i] = 1
            word[word.index(guess[i])] = ''
        
    return tuple(score)

def format_score(guess, score):
    """
    >>> print(format_score('hello', (0,0,0,0,0)))
     H  E  L  L  O  
    ⬜ ⬜ ⬜ ⬜ ⬜ 
    None
    >>> print(format_score('hello', (0,0,0,1,1)))
     H  E  L  L  O  
    ⬜ ⬜ ⬜ 🟨 🟨 
    None
    >>> print(format_score('hello', (1,0,0,2,1)))
     H  E  L  L  O  
    🟨 ⬜ ⬜ 🟩 🟨 
    None
    >>> print(format_score('hello', (2,2,2,2,2)))
     H  E  L  L  O  
    🟩 🟩 🟩 🟩 🟩 
    None
    """
    print(end=" ")
    for char in guess:
        print(char.upper(), end="  ")
    print()

    for digit in score:
        if digit == 2:
            print("🟩", end=" ")
        elif digit == 1:
            print("🟨", end=" ")
        else:
            print("⬜", end=" ")
    print()

def validate_score(score):
    """
    >>> validate_score((1,1,1,1,1))
    False
    >>> validate_score((2,2,2,2,1))
    False
    >>> validate_score((0,0,0,0,0))
    False
    >>> validate_score((2,2,2,2,2))
    True
    """
    win_condition = True

    for digit in score:
        if digit != 2:
            win_condition = False
            break
    return win_condition

def play(attempts):
    welcome()
    remaining_attempts = attempts

    while remaining_attempts > 0:
        guess = guess_input()
        score = score_guess(guess, secret_word)
        print(score)
        output = format_score(guess, score)
        if validate_score(score) == False:
            remaining_attempts -= 1
            print("Remaining Attempts: ", remaining_attempts)
            print()
            if remaining_attempts == 0:
                print("\nSorry, you lost. The word was: " + secret_word)
        else:
            print("\nYou won!")
            break

valid_words = generate_list(ALL_WORDS)
word_pool = generate_list(TARGET_WORDS)
secret_word = random.choice(word_pool)

def word_test():
    """
    >>> valid_words[0]
    'aahed'
    >>> valid_words[-1]
    'zymic'
    >>> valid_words[10:15]
    ['abamp', 'aband', 'abase', 'abash', 'abask']
    """

def main(test=False):
    if test:
        import doctest
        doctest_result = doctest.testmod()
        print(doctest_result)
        if doctest_result.failed == 0:
            print("Doctests passed!")
        else:
            print("Doctests failed!")
    play(GUESSES)

if __name__ == '__main__':
    print(main(test=True))
