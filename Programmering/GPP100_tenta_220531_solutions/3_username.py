# Anonymitetskod:
# Skriv en funktion som tar ett namn och returnerar ett användarnamn.
# Namnet ges på formatet "Efternamn, Förnamn". Användarnamnet ska
# bestå av de tre första bokstäverna i förnamnet följt av de tre
# första bokstäverna i efternamnet.
# Funktionen ska returnera en sträng som består av sex små bokstäver.
#
# Ex: Wayne, Bruce -> WAYne, BRUce -> BRU + WAY -> bruway
#
# Du kan anta att alla för- och efternamn har minst tre bokstäver,
# samt att inga för- eller efternamn innehåller mellanslag eller
# bindestreck. Mellan efter- och förnamn finns alltid exakt ett
# kommatecken och ett mellanslag.

def username(name):
    pos = name.find(' ')
    first = name[pos + 1:pos + 4].lower()
    second = name[:3].lower()
    return first + second


if __name__ == '__main__':
    print(username('Wayne, Bruce'))    # bruway
    print(username('Kyle, Selina'))    # selkyl
    print(username('Parker, Peter'))   # petpar
    print(username('Wells, Kristin'))  # kriwel
    print(username('Kent, Clark'))     # claken
