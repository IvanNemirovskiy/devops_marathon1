def extractor(extractable, value_type = str):
    n_d = dict(filter(lambda dictionary: isinstance(dictionary[1], value_type), extractable.items()))
    return n_d

