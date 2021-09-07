def raise_error(k, message):
        if k == "value":
            raise ValueError(message)
        elif k == "key":
            raise KeyError(message)
        elif k == "index":
            raise IndexError(message)
        elif k == "memory":
            raise MemoryError(message)
        elif k == "name":
            raise NameError(message)
        elif k == "eof":
            raise EOFError(message)
        else:
            raise ValueError("No error with such key.")
