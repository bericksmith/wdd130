import random

#Set a variable for the three difference tenses to use later in the program
tense = ["past", "present", "future"]

def main():
    """Program container uses the tense variable for two loops 
    to create the 6 sentences. Calls made to get_determiner, 
    get_verb, get noun, get_adjective, get_adverb and
    get_prepositional_phrase in each loop/.  
    
    The six sentences must have the following characteristics:

    Quantity	Verb Tense
    a.	single	past
    b.	single	present
    c.	single	future
    d.	plural	past
    e.	plural	present
    f.	plural	future
    """

    print()
    # loop through singular in past/present/future tense by calling the different functions that are included and print out what they return. 
    for tense_word in tense:
        determiner= get_determiner(1)
        verb= get_verb(1, tense_word)
        noun= get_noun(1)
        adjective= get_adjective()
        adverb= get_adverb()
        phrase= get_prepositional_phrase(1)
        print(f'{determiner.capitalize()} {adjective} {noun} {verb} {phrase} {adverb}.')

    # loop through plural in past/present/future tense by calling the different functions that are included and print out what they return.  
    for tense_word in tense:
        determiner= get_determiner(2)
        verb= get_verb(2, tense_word)
        noun= get_noun(2)
        adverb= get_adverb()
        phrase= get_prepositional_phrase(2)
        print(f'{determiner.capitalize()} {adjective} {noun} {verb} {phrase} {adverb}.')


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.

    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a noun.
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    # Randomly choose and return a verb.
    word = random.choice(words)
    return word

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    Parameters: None

    Return: a randomly chosen preposition.
    """
    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    # Randomly choose and return a preposition.
    word = random.choice(words)
    return word

def get_adjective():
    """Return a randomly chosen adjective
    from this list of prepositions:
        "good","new","great","little","attractive","beautiful"
    Parameters: None

    Return: a randomly chosen adjective.
    """
    words = ["good","new","great","little","attractive","beautiful"]

    # Randomly choose and return an adjective.
    word = random.choice(words)
    return word


def get_adverb():
    """Return a randomly chosen adjective
    from this list of prepositions:
        "quickly","smoothly","speedily","continually",
        "boldly","delightfully","hopelessly"
    Parameters: None

    Return: a randomly chosen adjective.
    """
    words = ["quickly","smoothly","speedily","continually","boldly","delightfully","hopelessly"]

    # Randomly choose and return an adverb.
    word = random.choice(words)
    return word


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or plural.
    Return: a prepositional phrase.
    """
    # Create a prepositional phrase using a preposition, determiner 
    # and a noun. Plural or singular determined by quantity variable.
    if quantity == 1:
        phrase =  (f"{get_preposition()} {get_determiner(1)} {get_noun(1)}")
    else:
        phrase =  (f"{get_preposition()} {get_determiner(2)} {get_noun(2)}")

    # return prepositional phrase
    return phrase

    
if __name__ == "__main__":
    main()










