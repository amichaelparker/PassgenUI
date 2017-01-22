''' Word testing functions '''

def caps_test(word):
    ''' Test words for capitalization '''

    if word[0] == word[0].upper():
        return True

    return False

def word_length(word, maximum, minimum):
    ''' Check that word length falls into requested bounds '''
    if minimum > maximum:
        minimum = maximum

    if minimum <= len(word) <= maximum:
        return True

    return False
