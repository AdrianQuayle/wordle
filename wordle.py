import random

ALL_WORDS = 'word-bank/all_words.txt'
TARGET_WORDS = 'word-bank/target_words.txt'
GUESSES = 6

def welcome():
    print("""   
    Welcome to Wordle!
    You have 6 tries to guess the five-letter word.
    Type your guess into the console and submit by pressing enter.
    A yellow tile indicated that you selected the right letter but it's in the wrong spot.
    A green tile indicates the correct letter in the correct spot.
    A grey tile indicated the selected letter is not included in the target word.
    """)

def get_valid_words():
    file = open(ALL_WORDS, 'r')
    valid_words = file.read().splitlines()
    file.close()
    return valid_words

def get_target_word():
    file = open(TARGET_WORDS, 'r')
    words = file.read().splitlines()
    file.close()
    return random.choice(words)

def guess_input():
    while True:
        try:
            guess = str(input("Guess the word: "))
            if len(guess) == 5:
                if guess in valid_words:
                    print(guess)
                    break
                else:
                    print("Invalid word")
            else:
                print("Input must be 5 characters long")
        except:
            print("Invalid input")
    return guess

def score_guess(guess, target_word):
    score = []
    i = 0
    for char in guess:
        if char == target_word[i]:
            score.append(2)
        elif char in target_word:
            score.append(1)
        else:
            score.append(0)
        i += 1
    return tuple(score)


valid_words = get_valid_words()
target_word = get_target_word()

print(get_target_word())
guess = guess_input()
print(score_guess(guess, target_word))
