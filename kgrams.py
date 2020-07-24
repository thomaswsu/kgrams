import random


markovmodel = {}
text = "the theremin in the basement is the theologian's theft detection device."
def get_kgram(text, position, k):
    if position+k>len(text):
        return text[position:]+text[:k-len(text[position:])]
    else:
        return text[position:(position+k)]
    """Returns the kgram starting at position in a text. For example:

    get_kgram("hello", 0, 3) would return "hel"
    get_kgram("hello", 1, 3) would return "ell"
    get_kgram("hello", 1, 4) would return "ello"
    get_kgram("hello", 3, 4) would crash since 3 + 4 is longer than the string."""


def process_character(m, text, position, k):
    if position <= len(text):
        if get_kgram(text, position, k) in m:
            if text[position + k] in m[get_kgram(text, position, k)]:
                m[get_kgram(text, position, k)][text[position+k]]+=1
            else:
                m[get_kgram(text, position, k)][text[position+k]]=1
        else:
            m[get_kgram(text, position, k)] = {text[position+k]:1}


    """Adds information about the given character to the model

    m is the model (a dictionary)
    text is the text
    text[position] is the character to be processed
    k is the order of our Markov chain"""

def build_markov_model(text, k):
    for i in range(len(text)-k):
        process_character(markovmodel, text, i, k)
    return markovmodel
    """ Returns the markov model for text.
    m is the model (a dictionary)
    text is the text
    k is the order of our Markov chain"""

def next_character_frequency(m, kgram, c):
    if  m.has_key(kgram):
        return m[kgram][c]
    else:
        return 0
    """ Returns the number of times c follows kgram
    m is the model (a dictionary)
    kgram is a kgram in in m
    c is a character that follows the given kgram"""

#delete later
m = build_markov_model(text, 3)


def random_character(m, kgram):
    lst = []
    for x in m[kgram]:
        for i in range(m[kgram][x]):
            lst.insert(0,x)
    return random.choice(lst)

    #"""returns a random character obeying markov model
    #m is the model (a dictionary)
    #kgram is a kgram in in m"""

def generate_random_text(m, N):
    seed = random.choice(m.keys())
    report = seed
    kgram1 = seed
    for i in range(N-len(seed)):
        kgram2 = random_character(m,kgram1)
        report += (kgram2)
        kgram1 = (kgram1[1:] + kgram2)
    return report


    #"""Returns A randomly generated text of length N
    #that obeys the probability distribution specified in m.

    #m is a Markov Model
    #N is the desired output length"""
