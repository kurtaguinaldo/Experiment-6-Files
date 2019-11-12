def getGuessedWord(secretWord,lettersGuessed):
    letters = ''
    for x in secretWord:
        if x in lettersGuessed:
             letters = letters + x
        else:
            letters = letters + "_"
    return letters