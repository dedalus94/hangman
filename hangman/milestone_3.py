import random 

word_list=['banana','apple','blueberries','raspberries','peach']
#print(word_list)

word=random.choice(word_list)
#print(word)

guess=input("please insert a letter:")


def ask_for_input():
    """ Ask for user's input """

    while True: 

        if len(guess)==1 and guess.isalpha():

            print("good guess!")
            break

        else: 

            print("Invalid letter. Please, enter a single alphabetical character.")



def check_guess(guess,word):

    """ Checks if the user input is in the secret word 
    
    Args: input letter, secred word 
    Output: print statement 
    
    """

    guess=guess.lower()


    if guess in word: 

        print(f"Good guess! {guess} is in the word.")

    else: 

        print(f"Sorry, {guess} is not in the word. Try again.")
