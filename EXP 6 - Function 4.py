
def isWordGuessed(secretWord,lettersGuessed):
     ans = all(elm in secretWord for elm in lettersGuessed)
     if ans:
        return True
     else:
        return False


def getGuessedWord(secretWord,lettersGuessed):
    letters = ''
    for x in secretWord:
        if x in lettersGuessed:
             letters = letters + x
        else:
            letters = letters + "_"
    return letters


def getAvailableLetters(lettersGuessed):
    
    import string
    alpha = string.ascii_lowercase
    
    z = ' '
    
    for x in alpha:
        if x in lettersGuessed:
             pass
        else:
             z+=x
    return z
        
        
        
def Hangaroo(secretWord):
    print("Let's Play Hangaroo!")
    size=len(secretWord)
    print("The word contains", size, "letters.")
    guesses = 5
    lettersGuessed=[]
    while (guesses !=0):
        if secretWord != getGuessedWord(secretWord,lettersGuessed):
            print("Available Letters : "),
            print(getAvailableLetters(lettersGuessed))
            print("You have", guesses,"chance/chances left.")
            print("Goodluck")
            g=input("Type a letter: ")
            guessInLowerCase = g.lower()
            
            if guessInLowerCase in lettersGuessed:
                print("Sorry,You already guessed this one.", getGuessedWord (secretWord, lettersGuessed))
                
            elif guessInLowerCase not in secretWord:
                print("The letter is not in the word", getGuessedWord (secretWord, lettersGuessed))
                print("Try Again")
                guesses = guesses - 1
                
            else:
                lettersGuessed.append(guessInLowerCase)
                print("Almost There!:",getGuessedWord(secretWord, lettersGuessed))
            lettersGuessed.append(guessInLowerCase)
        elif secretWord==getGuessedWord(secretWord, lettersGuessed):
            print ("Nice Job! You guessed the word, Want to Play Again?")
            break
        
    else:
        print("You have no more chances. Better luck next time!")
         
         