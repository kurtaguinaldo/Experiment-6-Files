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