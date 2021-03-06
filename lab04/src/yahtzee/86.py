def som(stenen):
    return sum(stenen)


def is_Yathzee(stenen):
    gesorteerde_stenen = sorted(stenen)
    return gesorteerde_stenen[0] == gesorteerde_stenen[-1]


def is_grote_straat(stenen):
    gesorteerde_stenen = sorted(stenen)
    for i in range(1, len(gesorteerde_stenen)):
        if gesorteerde_stenen[i] != gesorteerde_stenen[i - 1] + 1:
            return False
    return True


def is_kleine_straat(stenen):
    gesorteerde_stenen = sorted(stenen)
    tel = 1
    for i in range(1, len(gesorteerde_stenen)):
        if gesorteerde_stenen[i] == gesorteerde_stenen[i - 1] + 1:
            tel += 1
        else:
            if tel >= len(gesorteerde_stenen) - 1:
                return True
            if gesorteerde_stenen[i] != gesorteerde_stenen[i - 1]:
                tel = 1  # herbegin telling

    return tel >= len(stenen) - 1


def histogram(stenen):
    hist = {}
    for steen in sorted(stenen):
        if not steen in hist:
            hist[steen] = 0
        hist[steen] += 1
    return hist


def max_gelijk(stenen):
    hist = histogram(stenen)
    return max(hist.values())


def is_FullHouse(stenen):
    hist = histogram(stenen)
    #aantallen = sorted(hist.values(), reverse=True)
    #return aantallen[0] == 3 and aantallen[1] == 2
    return 2 in hist.values() and 3 in hist.values()

def grootste_score(stenen):
    if is_Yathzee(stenen):
        return 50
    if is_grote_straat(stenen):
        return 40
    if is_kleine_straat(stenen):
        return 30
    #3 gelijke of 4 gelijke of kans: score berekenen
    score = som(stenen)
    if score >= 25:
        return score
    if is_FullHouse(stenen):
        return 25
    return score