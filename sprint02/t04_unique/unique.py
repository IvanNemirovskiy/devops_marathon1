from collections import OrderedDict

def make_unique(dict_list: dict) -> str:
    d2 = {}

    for k, v in dict_list.items():
        d2[k] = list(set(v))

    for key, value in d2.items():
        d2[key] = sorted(value)
    return d2

