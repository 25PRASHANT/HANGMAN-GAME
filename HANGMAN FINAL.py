j# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 11:34:46 2019

@author: PRASHANT
"""

# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    a=len(secret_word)
    c=0
    for x in range(a):
        for y in range(a):
            if x!=a-y-1 and (a-y-1)>x:
                if secret_word[x]==secret_word[a-y-1]:
            
                 c+=-1
    b=0
    l=a+c
    for i in letters_guessed:
        for j in secret_word:
            if i==j:
                b+=1
                break
    
    return l==b
   
    



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    a=len(secret_word)
    b=len(letters_guessed)
    word=[]
    
    c=0
    for x in range(a):
        for y in range(b):
#            if x!=a-y-1 and (a-y-1)>x:
                if secret_word[x]==letters_guessed[y]:
                    word.append(secret_word[x])
                    break
                
                
        else:        
            word.append("_ ")
                
                
    return(''.join(word))
    



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    a=string.ascii_lowercase
    b=letters_guessed
    c=list(a)
    d=list(b)
    z=[]
    for i in c:
        for j in d:
            if i==j:
                z.append(i)
    for i in range(len(z)):
        c.remove(z[i])
        
    return (''.join(c))
    
def unique_words(secret_word):
    a=len(secret_word)
    c=0
    for x in range(a):
        for y in range(a):
            if x!=a-y-1 and (a-y-1)>x:
                if secret_word[x]==secret_word[a-y-1]:
            
                 c+=-1
    b=0
    l=a+c
    return l    
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    b=list(my_word)
    
    c=0
    d=0
    for i in b:
        if i==" ":
            c+=1
    for i in range(c):
        b.remove(" ")
        
    word=''.join(b)
    
    
#len_word=len(word)
#len_other_word=len(other_word)

    for i in range(len(word)):
        for j in range(len(other_word)):
            if i==j and word[i]==other_word[j]:
                d+=1
                break
            
    return (d==(len(word)-c) and len(word)==len(other_word))
       
    





def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    
    
    
    
    
    b=list(my_word)
    c=0
    d=0
    new_list=[]
    for i in b:
        if i==" ":
            c+=1
    for i in range(c):
        b.remove(" ")
    word=''.join(b)
    for q in wordlist:
        d=0
        if len(word)==len(q):
             for i in range(len(word)):
                 for j in range(len(q)):
                     if i==j and word[i]==q[j]:
                         d+=1
                         break
        if d==(len(word)-c) and len(word)==len(q):
            new_list.append(q)
    return new_list
    
    
    
    
    
#    



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


#if __name__ == "__main__":
#    # pass
#
#    # To test part 2, comment out the pass line above and
#    # uncomment the following two lines.
#    
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
#secret_word="apple"
print("Welcome to the game Hangman!")
print("I am thinking of a word that is 5 letters long.")
print("you have 3 warnings left")
print("you have 6 guesses left")
print("Available letters: abcdefghijklmnopqrstuvwxyz")
warnings=4
guesses=6
m=1
letters_guessed=''
for e in range(20):
    letter_raw=input("Please guess a letter:")
#letter=letter_raw.lower()
    if letter_raw.isalpha():
        letter=letter_raw.lower()
        for w in letters_guessed :
            if w==letter:
                print("the letter has already been guessed")
                warnings+=-1
                print("you have",warnings," warnings left")
#                print("You have",guesses,"guesses left.")
                break
        if warnings<=0:
            guesses+=-1
            print("You have",guesses,"guesses left.")
            
        if guesses<=0:
            print("game over.... you lose")
            break
        for r in letters_guessed:
            m=1
            if letter==r:
                m=0
            else:
                m=1
        if m==1:
            letters_guessed+=letter        
        for q in secret_word:
            if q==letter:
                print("Good guess:",get_guessed_word(secret_word, letters_guessed))
                print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                print("You have",guesses,"guesses left.")
                print("Available letters:", get_available_letters(letters_guessed))
                break
        if is_word_guessed(secret_word, letters_guessed):
            print("Hurray!! the word has been guessed")
            print("your score is",guesses*unique_words(secret_word))
            break
                
            
        elif q!=letter and m==1:
                print("Oops! That letter is not in my word:")
                print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                guesses+=-1
                print("You have",guesses,"guesses left.")
                print("Available letters:", get_available_letters(letters_guessed))
    else:
        if letter_raw=="*":
             my_word=get_guessed_word(secret_word, letters_guessed)
             print("possible guesses are:")
             print(show_possible_matches(my_word))
             print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
             print("you have",guesses,"guesses left")
             print("Available letters:", get_available_letters(letters_guessed))
        else:                
            warnings+=-1
            print("Oops! That is not a valid letter. You have",warnings," warnings left:")
            if warnings<=0:
                guesses+=-1
                print("You have",guesses,"guesses left.")
        
            if guesses<=0:
                print("game over.... you lose")
                break




#my_word="t_ _ t"
#print(show_possible_matches(my_word))    