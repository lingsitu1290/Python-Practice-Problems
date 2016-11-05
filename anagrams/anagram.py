"""Given a list of words, return the word with the most anagrams.

For a list of ['act', 'cat', 'bill']:
- 'act' and 'cat' are anagrams, so they both have 2 matching words.
- 'bill' has no anagrams, os it has one matching word (itself).

Given that 'act' is the first instance of the most-anagrammed word,
we return that.

    >>> find_most_anagrams_from_wordlist(['act', 'cat', 'bill'])
    'act'

Let's use a file of words where each line is a word:

    >>> all_words = [w.strip() for w in open('words.txt')]
    >>> find_most_anagrams_from_wordlist(all_words)
    'angor'

"""


def make_anagram_dict(words):

    anagram_dict = {}

    # create dictionary of sorted word and it's associated anagram list
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]

    return anagram_dict

def find_most_anagrams_from_wordlist(wordlist):
    """Given list of words, return the word with the most anagrams."""

    all_anagrams_dict = make_anagram_dict(wordlist)

    max_length = 0
    most_anagrams = None

    # for each sorted word, if the length of its anagram list is greater than the 
    # max return the most_anagram word.
    for word in wordlist:
        sorted_word = "".join(sorted(word))
        length = len(all_anagrams_dict[sorted_word])
        if length > max_length:
            max_length = length
            most_anagrams = word

    return most_anagrams


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
