import random 

class Hangman: 

    def __init__(self,word_list):

        self.num_lives = 5 
        self.word_list = word_list 
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word)-set(self.word_guessed)) # character _ will automatically not be counted!  
        self.list_of_guesses = []

    def check_guess(self,guess):

        """ 
            Checks if the user input is in the secret word 
    
            Args: input letter, secred word 
            Output: print statement 

        """
        guess=guess.lower()

        if guess in self.word: 

            print(f"Good guess! {guess} is in the word.")

        else: 

            print(f"Sorry, {guess} is not in the word. Try again.")


    def ask_for_input(self):

        """ Ask for user's input """

        while True: 
            
            guess=input("please guess a letter:") 

            if not (len(guess)==1 and guess.isalpha()):

                print("Invalid letter. Please, enter a single alphabetical character.")

            elif guess in self.list_of_guesses:

                print("You already tried that letter!")

            else: 

                self.check_guess(guess)



hm=Hangman(['apple','banana','orange','melon'])

hm.ask_for_input()
                


print(hm.num_live)
print(hm.word_list)
print(hm.word)
print(hm.word_guessed)
print(hm.num_letters)
print(hm.list_of_guesses) 




