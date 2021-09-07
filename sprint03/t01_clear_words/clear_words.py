import re


def clear_words(arg):
    n_l = arg.split(' ')
    res = lambda rmP: re.sub(r"[?!.:;,-]", '', rmP)

    return list(map(res, n_l))