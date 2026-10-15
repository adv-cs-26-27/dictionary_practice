"""
dictionary notes!

definition: 
like a list -- but uses "keys" to access information as opposed to indices
the keys must be immutable: strings, ints, and tuples all work, but NOT LISTS
the values can be basically anything -- lists, another dictionary, integers, strings, etc!

creating a new dictionary:
my_empty_dictionary = {}
see letterScoreDict below for an example of a fully-formed dictionary

access a value in a dictionary:
dictionary_name["key"]
ex. letterScoreDict['q'] would give us 10

update a value in a dictionary:
very similar to accessing the value, just an equals sign and the new value
ex. letterScoreDict['q'] = 20 would update 'q' to have a value of 20

add a new key/value pair to a dicitionary:
ex. letterScoreDict['1'] = 5
basically the same as updating, just with a key that does not exist yet

checking if a key exists in a dictionary:
if "key" in my_dictionary:

"""


### DICTIONARY PRACTICE PROBLEMS -- all problems should be solved using a dictionary! ###

letterScoreDict =  {'a': 1,  'b': 3,  'c': 3,  'd': 2,  'e': 1,
                    'f': 4,  'g': 2,  'h': 4,  'i': 1,  'j': 8,
                    'k': 5,  'l': 1,  'm': 3,  'n': 1,  'o': 1,
                    'p': 3,  'q': 10, 'r': 1,  's': 1,  't': 1,
                    'u': 1,  'v': 4,  'w': 4,  'x': 8,  'y': 4,
                    'z': 10 }

def scrabbleScore(word):
    """
    scrabbleScore(word) should take a string argument word, 
    which can have any characters, and should return the 
    Scrabble score of that string.
    """
    # TODO: complete this function
    return 0

#
# scrabbleScore Tests
#
def scrabbleScoreTests():
    print( "scrabbleScore('quetzal')           should be  25 :",  scrabbleScore('quetzal') )
    print( "scrabbleScore('jonquil')           should be  23 :",  scrabbleScore('jonquil') )
    print( "scrabbleScore('syzygy')            should be  25 :",  scrabbleScore('syzygy') )
    print( "scrabbleScore('?!@#$%^&*()')       should be  0 :",  scrabbleScore('?!@#$%^&*()') )
    print( "scrabbleScore('')                  should be  0 :",  scrabbleScore('') )
    print( "scrabbleScore('abcdefghijklmnopqrstuvwxyz') should be  87 :",  scrabbleScore('abcdefghijklmnopqrstuvwxyz') )
    print( "scrabbleScore('a')                 should be  1 :",  scrabbleScore('a') )   # single letter
    print( "scrabbleScore('qi')                should be  11 :",  scrabbleScore('qi') )
    print( "scrabbleScore('zzz')               should be  30 :",  scrabbleScore('zzz') )   # repeated letters each count
    print( "scrabbleScore('jazz')              should be  29 :",  scrabbleScore('jazz') )
    print( "scrabbleScore('cat123')            should be  5 :",  scrabbleScore('cat123') )   # digits score 0
    print( "scrabbleScore('hello world!')      should be  17 :",  scrabbleScore('hello world!') )   # spaces/punctuation score 0
    print( "scrabbleScore('oxyphenbutazone')   should be  41 :",  scrabbleScore('oxyphenbutazone') )

# TODO: call the test function to confirm your function works correctly!

#--------------------------------------------------------------#

"""
TODO: Write a function transcribe(dna), which should take an argument that is a string dna, 
of DNA nucleotides (capital letter As, Cs, Gs, and Ts). [There may be other characters, 
too, though they should be ignored by your transcribe function by simply disappearing 
from the return value. These might be spaces or other characters that are not 
really DNA nucleotides.]

transcribe should return the messenger RNA that would be produced from that string S. 
The correct return value simply uses replacement:

    As in the argument become Us in the result.
    Cs in the argument become Gs in the result.
    Gs in the argument become Cs in the result.
    Ts in the argument become As in the result.
    any other input characters should disappear from the result altogether

You may want to create a helper function that converts one nucleotide at a time. 
A dictionary works well here! 
"""

def transcribe(dna):
    # TODO: complete this function
    pass

#
# Tests
#
def transcribeTests():
    print( "transcribe('ACGTTGCA') should be  'UGCAACGU' :",  transcribe('ACGTTGCA') )
    print( "transcribe('ACG TGCA') should be  'UGCACGU' :",  transcribe('ACG TGCA') )  # Note that the space disappears
    print( "transcribe('GATTACA')  should be  'CUAAUGU' :",  transcribe('GATTACA') )
    print( "transcribe('cs5')      should be  ''  :",  transcribe('cs5') ) # Note that other characters disappear
    print( "transcribe('')         should be  '' :",  transcribe('') )   # Empty strings!
    print( "transcribe('A')        should be  'U' :",  transcribe('A') )   # single nucleotide
    print( "transcribe('AAAA')     should be  'UUUU' :",  transcribe('AAAA') )
    print( "transcribe('TTTT')     should be  'AAAA' :",  transcribe('TTTT') )
    print( "transcribe('CCGG')     should be  'GGCC' :",  transcribe('CCGG') )
    print( "transcribe('A-C-G-T')  should be  'UGCA' :",  transcribe('A-C-G-T') )   # dashes disappear
    print( "transcribe('acgtACGT') should be  'UGCA' :",  transcribe('acgtACGT') )   # lowercase letters disappear
    print( "transcribe('12345')    should be  '' :",  transcribe('12345') )   # nothing valid at all
    print( "transcribe('ATG CCC TAA') should be  'UACGGGAUU' :",  transcribe('ATG CCC TAA') )

# TODO: call the test function to confirm your function works correctly!

#--------------------------------------------------------------#

"""
TODO: Write a function, bananagrams, that takes two arguments, a list of letters 
and a word, and returns a boolean indicating whether the word can be made from 
the list of letters. For example, calling banagrams(["I", "T", "B"], "BIT") should 
return True, but banagrams(["I", "T", "B"], "BIB") should return False.
"""

def bananagrams(letters, word):
    # TODO: complete this function
    pass

#
# Tests
#
def bananagramsTest():
    print( "bananagrams(['I', 'T', 'B'], 'BIT')       should be  True :",  bananagrams(['I', 'T', 'B'], 'BIT') )
    print( "bananagrams(['I', 'T', 'B'], 'BIB')       should be  False :",  bananagrams(['I', 'T', 'B'], 'BIB') )   # only one B
    print( "bananagrams(['B', 'I', 'T', 'S'], 'BIT')  should be  True :",  bananagrams(['B', 'I', 'T', 'S'], 'BIT') )   # leftover letters are fine
    print( "bananagrams(['B', 'I', 'T'], 'BITS')      should be  False :",  bananagrams(['B', 'I', 'T'], 'BITS') )   # missing a letter
    print( "bananagrams(['B', 'I', 'B', 'T'], 'BIB')  should be  True :",  bananagrams(['B', 'I', 'B', 'T'], 'BIB') )   # duplicate letters available
    print( "bananagrams(['A', 'A', 'A'], 'AAAA')      should be  False :",  bananagrams(['A', 'A', 'A'], 'AAAA') )   # not enough copies
    print( "bananagrams(['L', 'E', 'P', 'P', 'A'], 'APPLE') should be  True :",  bananagrams(['L', 'E', 'P', 'P', 'A'], 'APPLE') )   # order doesn't matter
    print( "bananagrams(['P', 'L', 'E', 'A'], 'APPLE')      should be  False :",  bananagrams(['P', 'L', 'E', 'A'], 'APPLE') )   # needs two Ps
    print( "bananagrams(['A', 'B'], '')               should be  True :",  bananagrams(['A', 'B'], '') )   # empty word can always be made
    print( "bananagrams([], '')                       should be  True :",  bananagrams([], '') )   # empty everything
    print( "bananagrams([], 'A')                      should be  False :",  bananagrams([], 'A') )   # no letters to use

# TODO: call the test function to confirm your function works correctly!