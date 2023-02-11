from sentences import get_determiner, \
    get_noun, get_verb, get_preposition,\
    get_adjective, get_prepositional_phrase

import random
import pytest

def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # 1. Test the single noun.

    single_noun = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 11 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(11):

        # Call the get_noun function which
        # should return a single noun.
        word = get_noun(1)

        # Verify that the word returned from get_noun
        # is one of the words in the single_noun list.
        assert word in single_noun

    # 2. Test the plural determiners.

    plural_noun = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 11 times.
    for _ in range(11):

        # Call the get_noun function which
        # should return a plural noun.
        word = get_noun(2)

        # Verify that the word returned from noun
        # is one of the words in the plural_noun list.
        assert word in plural_noun

def test_get_verb():
    
    single_past_verb = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(11):

        word = get_verb(1, "past")
        assert word in single_past_verb

    single_present_verb = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(11):

        word = get_verb(1, "present")
        assert word in single_present_verb  
    
    plural_present_verb = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]

    for _ in range(11):

        word = get_verb(2, "present")
        assert word in plural_present_verb

    future_verb = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    for _ in range(11):

        word = get_verb(1, "future")
        assert word in future_verb

def test_get_preposition():
    preposition = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    for _ in range(31):

        word = get_preposition()
        assert word in preposition

def test_get_adjective():
    adjective = ["good","new","great","little","attractive","beautiful"]

    for _ in range(7):

        word = get_adjective()
        assert word in adjective

def test_get_prepositional_phrase():

    phrase =  get_prepositional_phrase(1)
    x = phrase.split()

    assert len(x) == 3
 
    phrase_plural =  get_prepositional_phrase(2)
    y = phrase_plural.split()
    
    assert len(y) == 3

  





    

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])