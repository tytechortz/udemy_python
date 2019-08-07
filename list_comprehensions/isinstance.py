def zeroes(stuff):
    return [x if not isinstance(x, str) else 0 for x in stuff]