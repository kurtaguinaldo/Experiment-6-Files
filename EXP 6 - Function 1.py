def isWordGuessed(secretWord,lettersGuessed):
    ans = all(elm in secretWord for elm in lettersGuessed)
    if ans:
        return True
    else:
        return False