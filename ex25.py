"""Functions to do words stuff"""


def break_words(stuff):
    """Break sentense into words"""
    words = stuff.split(" ")
    return words


def sort_words(words):
    """Sort words"""
    return sorted(words)


def print_first_word(words):
    """Pop and print 1st word"""
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """Pop and print last word"""
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """Takes a sentence and return sorted words"""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints 1st and last words of sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Prints 1st and last of sorted words"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
