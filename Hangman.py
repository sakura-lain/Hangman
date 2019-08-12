print("Welcome to Hangman game!")

print(" Hangman rules: \n"
    +"I have a secret word \n"
    +"You need to guess each letter in the word \n" 
    +"If your guess matches the secret word letter then you win\n"
    +"If your guess does not match the secret word letter then you loose\n"
    +"and you will make a step forward to be hanged.\n")


def get_name():
    name=input('What is your name?')
    if (name.isdigit()):
        print('No digit in name, please.')
        get_name()
    else:
        get_guess()

import random
words=["ironhack", "computer", "team", "beer", "weekend"]
secret_word = random.choice(words)

def get_guess():
    dashes = "-" * len(secret_word)
    guesses_left=len(secret_word)+3
    
    while guesses_left>-1 and not dashes == secret_word:
        print(dashes)
        print(str(guesses_left))
        
        guess = input("Make your guess: ")

        
        if len(guess)!=1:
            print('Your guess should have at least 1 character')
        elif (guess.isdigit()):
            print('No digit in guess, please.')#elif type(guess)!=str:
         #   print('Your guess should be a letter')
        elif guess not in secret_word:
            print('This letter is not in the secret word!')
            guesses_left -=1
        else:
            print('This letter is in the secret word!')
            dashes = update_dashes(secret_word, dashes, guess)
            guesses_left -=1
            
    if guesses_left<0:
        print('You lose! The secret word was', str(secret_word), '.\n' 'You are hung!')
    else:
        print('Congratulations! You win! The secret word was',str(secret_word),'.')            

def update_dashes(secret, cur_dash, rec_guess):
    result = ""
    for i in range(len(secret)):
        if secret[i] == rec_guess:
            result = result + rec_guess     
        else:
            result = result + cur_dash[i]
    return result

get_name()
get_guess()
