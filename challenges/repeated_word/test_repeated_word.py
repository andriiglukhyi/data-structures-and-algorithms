from hash_table import HashTable
from repeated_word import repeated_word


small = "Once upon a time, there was a brave princess who..."
big = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
new = "It was a queer sultry summer the summer they electrocuted the Rosenbergs and I didn’t know what I was doing in New York"

def test_empty_string():
    """test when argument are empty string"""
    assert repeated_word('') is False
    assert repeated_word('me') is False 


def test_small_string():
    """test small string"""
    assert repeated_word(small) == 'a'


def test_big_string():
    """test bif string"""
    assert repeated_word(big) == "it"


def test_new_string():
    """test one more string"""
    assert repeated_word(new) == "summer"


