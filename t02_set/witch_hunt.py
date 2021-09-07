def witch_hunt(suspect_sets: set, innocent_sets: set) -> set:
    witch = set([])
    for i in suspect_sets:
        if witch:
            witch = witch.intersection(i)
        else:
            witch = i.copy()
    for i in innocent_sets:
        witch = witch.difference(i)
    return witch
