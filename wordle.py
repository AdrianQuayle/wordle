file = open('word-bank/all_words.txt')
lines = file.read().splitlines()
valid_words = lines.copy()
file.close()

def welcome():
    print("""   
    Welcome to Wordle!
    You have 6 tries to guess the five-letter word.
    Type your guess into the console and submit by pressing enter.
    A yellow tile indicated that you selected the right letter but it's in the wrong spot.
    A green tile indicates the correct letter in the correct spot.
    A grey tile indicated the selected letter is not included in the target word.
    """)

def guess_input():
    while True:
        try:
            guess = str(input('Guess the word: '))
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

welcome()
guess_input()