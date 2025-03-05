# Skriv en funktion som tar ett ord (string) som input och returnerar samma ord men med alla
# vokaler skrivna med stor bokstav och alla konsonanter med liten bokstav.
# Funktionen ska inte ta hänsyn till små och stora bokstäver i det ursprungliga ordet.
def uppercase_vowels(word):
    vowels = {'a', 'o', 'u', 'å', 'e', 'i', 'y', 'ä', 'ö'}
    res = ''
    for letter in word:
        if letter.lower() in vowels:
            res += letter.upper()
        else:
            res += letter.lower()
    return res


if __name__ == '__main__':
    print(uppercase_vowels('lekstuga'))    # lEkstUgA
    print(uppercase_vowels('ängel'))    # ÄngEl
