# I spelet scrabble beräknas ordpoängen genom att poängen för varje bokstav i ordet adderas.
# Beroende på språk kan antalet poäng per bokstav variera.
# Skriv en funktion som tar ett ord samt en dict med antal poäng per bokstav och returnerar ordpoängen.
# Funktionen ska inte göra någon skillnad på små och stora bokstäver. Du kan anta att bokstäverna
# i dict:en är små.
def scrabble_score(word, letter_scores):
    score = 0
    for letter in word:
        score += letter_scores[letter.lower()]
    return score


if __name__ == '__main__':
    tile_dict = { 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
                  'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
                  'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10 }
    print(scrabble_score('Quiz', tile_dict))     # returnerar 22 (= 10 + 1 + 1 + 10)
    print(scrabble_score('consanguineous', tile_dict))
    print(scrabble_score('incomprehensibilities', tile_dict))
    print(scrabble_score('oxyphenbutazone', tile_dict))
    print(scrabble_score('jukebox', tile_dict))

    sv_dict = {'a': 1, 'b': 4, 'c': 8, 'd': 1, 'e': 1, 'f': 4, 'g': 2, 'h': 3, 'i': 1, 'j': 8,
               'k': 3, 'l': 1, 'm': 3, 'n': 1, 'o': 2, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
               'u': 3, 'v': 4, 'x': 10, 'y': 8, 'z': 10, 'å': 4, 'ä': 4, 'ö': 4}
    print(scrabble_score('jukebox', sv_dict))
    print(scrabble_score('blåbyxa', sv_dict))
    print(scrabble_score('upptryck', sv_dict))
    print(scrabble_score('snusnäsduk', sv_dict))
