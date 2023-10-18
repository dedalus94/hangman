import random 

class Hangman: 

    def __init__(self,word_list ):

        self.num_lives = 5 
        self.word_list = word_list 
        self.word=random.choice(self.word_list)
        self.word_guessed=['_']*len(self.word)
        self.num_letters= len(set(word)-set(word_guessed)) # character _ will automatically not be counted!  
        self.list_of_guesses=[]