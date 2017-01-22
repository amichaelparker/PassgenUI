''' Assemble password from word list '''

import random
from lib import wordcheck as wc

def pass_gen(length, caps, maximum, minimum, special, digit):
    ''' Concatenate words from list, adding special characters and digits if requested '''

    s_characters = '!@#$%^&*~'
    i_digits = '1234567890'

    password = ''

    for _ in range(length):
        new_word = ''

        if caps:
            new_word = random.choice(open('lib/words.txt').readlines()).rstrip()
            while not wc.word_length(new_word, maximum, minimum):
                new_word = random.choice(open('lib/words.txt').readlines()).rstrip()
        else:
            new_word = random.choice(open('lib/words.txt').readlines()).rstrip()
            while wc.caps_test(new_word) or not wc.word_length(new_word, maximum, minimum):
                new_word = random.choice(open('lib/words.txt').readlines()).rstrip()

        password += new_word

    if digit:
        password += i_digits[int(random.random() * len(i_digits))]

    if special:
        password += s_characters[int(random.random() * len(s_characters))]

    return password
