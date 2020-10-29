def charFrequency(s):
    sdv, sef = [(x, s.count(x)) for x in s], []
    [sef.append(y) for y in sdv if sef.count(y) == 0]
    sef.sort(key=lambda x: x[1], reverse=True)
    return sef