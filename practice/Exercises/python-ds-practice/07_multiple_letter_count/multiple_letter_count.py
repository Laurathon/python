def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    dic_phrase =list(phrase).copy()   # put in a list
    dict = {}
    i=0
    for ltr in dic_phrase:  
        keys = dict.keys()          
        if ltr in keys:
            dict[ltr] +=1
        else:
            dict[ltr] =1

    return dict

