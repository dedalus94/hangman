import random 

class Hangman: 

    def __init__(self,word_list,num_lives):

        self.num_lives = num_lives 
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

            for idx, letter in enumerate(self.word):

                if letter==guess: 

                    print(idx,self.word_guessed)
                    self.word_guessed[idx]==guess
                    print(self.word_guessed)
            
            self.num_letters-=1
            print(self.word_guessed)

        else: 

            print(f"Sorry, {guess} is not in the word. Try again.")

            self.num_lives-=1

            print(f"You have {self.num_lives} lives left.")


    def ask_for_input(self):

        """ Ask for user's input """
            
        guess=input("please guess a letter:") 

        if not (len(guess)==1 and guess.isalpha()):

            print("Invalid letter. Please, enter a single alphabetical character.")

        elif guess in self.list_of_guesses:

            print("You already tried that letter!")

        else: 

            self.check_guess(guess)


def play_game(word_list):

    num_lives = 5 
    game = Hangman(word_list,num_lives)

    while True: 

        if num_lives==0: 

            print("you lost!")
            break

        if game.num_letters > 0: 

            game.ask_for_input()

            if num_lives>0 and game.num_letters==0:

                print("You won the game!")
                break



play_game(['apple','banana','orange','melon'])


        
