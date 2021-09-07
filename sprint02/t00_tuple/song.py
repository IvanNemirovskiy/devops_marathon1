def song(verses : tuple, chorus: tuple) -> tuple:
    output = ()
    if isinstance(verses, tuple) and isinstance(chorus, tuple):
        for v in verses:
            output += v + chorus
        return  output + chorus