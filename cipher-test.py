from cipher import *

#test the generate pad function:
#test whether all characters in the pad are capitalized
def test_generatePad_upper():
    assert generatePad(1200).isupper() == True

#test whether the length of the pad is the same as the input number
def test_generatePad_length():
    assert len(generatePad(1200)) == 1200

#test the encipher function:
#test whether a simple translation of the word "HELLO" using a simple pad is correct
def test_encipher_hello():
    assert encipher("GHIJKLMNOPQRSTUVWXYZ", "HELLO") == "NLTUY"

#test whether the program can ignore punctuations, still translating "HELLO" and using the same pad as before
def test_encipher_hello_ignore():
    assert encipher("GHIJKLMNOPQRSTUVWXYZ", "HE! &LLO") == "NLTUY"

#test the decipher function:
#test whether the program and translate back to the original word, still using the same pad and "HELLO"
def test_decipher_hello():
    assert decipher("GHIJKLMNOPQRSTUVWXYZ", "NLTUY") == "HELLO"

#test whether the program and translate back to the original word and ignore punctuations, still using the same pad and "HELLO"
def test_decipher_hello_ignore():
    assert decipher("GHIJKLMNOPQRSTUVWXYZ", "NL! *TUY") == "HELLO"