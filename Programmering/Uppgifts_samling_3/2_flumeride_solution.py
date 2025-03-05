# För att få åka attraktionen FlumeRide måste man vara minst 130 cm lång eller
# minst 100 cm i vuxens sällskap. Skriv en funktion som tar ett heltal som
# representerar personens längd och en boolean som representerar vuxens sällskap.
# Funktionen ska returnera en boolean som säger om personen får åka (True) eller
# inte (False).

def flumeride(length, accompanied):
    if length >= 130 or (length >= 100 and accompanied):
        return True
    else:
        return False


if __name__ == '__main__':
    print(flumeride(136, False))   # True
    print(flumeride(123, False))   # False
    print(flumeride(98, True))     # False

    below = list(range(70, 100))
    between = list(range(100, 130))
    above = list(range(130, 200))
    for length in below:
        assert not flumeride(length, True)
        assert not flumeride(length, False)
    for length in between:
        assert flumeride(length, True)
        assert not flumeride(length, False)
    for length in above:
        assert flumeride(length, True)
        assert flumeride(length, False)
