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

def generate_list(file_path):
    file = open(file_path, 'r').read().splitlines()
    return file

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

def score_guess(guess, secret_word):
    score = []
    i = 0
    for char in guess:
        if char == secret_word[i]:
            score.append(2)
        elif char in secret_word:
            score.append(1)
        else:
            score.append(0)
        i += 1
    return tuple(score)


valid_words = generate_list(ALL_WORDS)
word_pool = generate_list(TARGET_WORDS)
secret_word = random.choice(word_pool)

print(secret_word)
guess = guess_input()
print(score_guess(guess, secret_word))
