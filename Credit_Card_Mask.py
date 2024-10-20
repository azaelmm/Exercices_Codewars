def maskify(s):
    if len(s) <= 4:
        return s
    return '#' * (len(s) - 4) + s[-4:]
