import random

logo = """
 __          __  _                            _          _    _                                           _ 
 \ \        / / | |                          | |        | |  | |                                         | |
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __   | |
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  | |
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |  | | (_| | | | | (_| | | | | | | (_| | | | | |_|
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| (_)
                                                                             __/ |                          
                                                                            |___/                                             
"""

win = """
 __     ______  _    _  __          _______ _   _   _ 
 \ \   / / __ \| |  | | \ \        / /_   _| \ | | | |
  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| | | |
   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` | | |
    | | | |__| | |__| |    \  /\  /   _| |_| |\  | |_|
    |_|  \____/ \____/      \/  \/   |_____|_| \_| (_)                                                      
"""

lose = """
 __     ______  _    _   _      ____   _____ ______   _ 
 \ \   / / __ \| |  | | | |    / __ \ / ____|  ____| | |
  \ \_/ / |  | | |  | | | |   | |  | | (___ | |__    | |
   \   /| |  | | |  | | | |   | |  | |\___ \|  __|   | |
    | | | |__| | |__| | | |___| |__| |____) | |____  |_|
    |_|  \____/ \____/  |______\____/|_____/|______| (_)                                                                                    
"""

hang_stages = [
"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |                       
    |                           
    |                            
    |___                    
    HA _ _ _ _ _""",

"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    HAN _ _ _ _""",


"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    HANG _ _ _""",


"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    HANGM _ _""",



"""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    HANGMA _""",


"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    HANGMAN"""

]


class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.


    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has

    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, misses, num_lives):
        # TODO 2: Initialize the attributes as indicated in the docstring
        self.word_list = word_list
        self.num_lives = num_lives
        self.secret_word = random.choice(word_list)
        self.num_letters = len(set(self.secret_word))
        self.guessed_word = []
        self.list_letters = []
        self.misses = misses # Number of chances the user misses to guess the letter
        
        # TODO 2: Print two message upon initialization:
        # 1. "The mistery word has {num_letters} characters"
        # 2. {word_guessed}
        # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter

        for w in range(len(self.secret_word)):
            self.guessed_word.append(' - ')
        print(f'\nThe mistery word has {self.num_letters} letters. \n')
        print(f"\n{self.guessed_word} \n")

    def check_letter(self, user_guessed_letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked
        '''
        # TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase
        for l in range(len(self.secret_word)):
           if user_guessed_letter.lower() in self.secret_word[l]:
             self.guessed_word[l] = user_guessed_letter
        
        # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
        if user_guessed_letter.lower() in self.secret_word:
            self.num_letters -= 1
            print(f"\n{self.guessed_word} \n")
            print(f"\nYour guess {user_guessed_letter} is correct. You have {self.num_letters} letters left to guess. \n")
            print('\nYou have got ' + str(self.num_lives) + ' number of lives!\n')
       
        # TODO 3: If the letter is not in the word, reduce the number of lives by 1
        elif user_guessed_letter.lower() not in self.secret_word:
            self.num_lives -= 1
            print(self.guessed_word)
            print(f"\nYour guess {user_guessed_letter} is incorrect. You have {self.num_lives} lives left. \n")
            self.misses += 1
            print("\n", hang_stages[self.misses], "\n")
            
        pass

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter
        while True:
                        
            # TODO 1: Assign the letter to a variable called `letter`
            self.user_guessed_letter = str(input('Please guess a letter: \n \n'))
            
            # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
            if len(self.user_guessed_letter) > 1:
                print("Please, enter just ONE letter! \n")

            # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried".
            # Be careful! A letter can contain the same letter more than once. TIP: Take a look at the index() method in the string class
            elif self.user_guessed_letter in self.list_letters:
                print("\n", hang_stages[self.misses], "\n")
                print("\n" f"{self.user_guessed_letter} was already used! \n")
            
            # TODO 3: If the letter is valid, call the check_letter method
            else:
                self.list_letters.append(self.user_guessed_letter)
                Hangman.check_letter(self, self.user_guessed_letter)

            # If the user guesses the word, print "Congratulations! You won!"
            if self.num_letters == 0:
                print("Congratulations! You won!" "\n\n", win, "\n\n")
                break
            
            # If the user runs out of lives, print "You lost! The word was {word}"
            if self.num_lives == 0 or self.misses == 5:
                print(f"Sorry, the word was {self.secret_word}.\n" "\n\n", lose, "\n\n")
                break            
                
                pass


if __name__ == '__main__':
    print ("\n \n", logo,"\n")
    print(hang_stages[0])    
    
    # As an aid, part of the code is already provided:
    word_list = ['apple', 'banana', 'orange',
                 'pear', 'strawberry', 'watermelon']
    game = Hangman(word_list, misses=0, num_lives=5)
    print(f'\nYou have got 5 number of lives!\n')
    game.ask_letter()

    # TODO 1: To test this task, you can call the ask_letter method
    # TODO 2: To test this task, upon initialization, two messages should be printed
    # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word
    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
pass
