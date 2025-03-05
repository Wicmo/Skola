# Skriv en funktion som får en text som input och returnerar en dict som innehåller alla unika ord
# i texten och deras frekvens (hur många gånger de finns i texten).
# Funktionen behöver bara hantera ord med endast små bokstäver. Vi kan anta att det inte finns
# några skiljetecken i texten, bara ord skilda åt av mellanslag.
def frequencies(text):
    freq = {}
    word_list = text.split()
    for word in word_list:
        word = word.lower()
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq


if __name__ == '__main__':
    ordsallad = 'det var en gång en gång och det var det det var'
    print(frequencies(ordsallad))  # {'det': 4, 'var': 3, 'en': 2, 'gång': 2, 'och': 1}
    song = 'na na na na na na na na na na na na na na na na batman'
    print(frequencies(song))       # {'na': 16, 'batman': 1}
    phrase = 'what he had had had had an affect on me'
    print(frequencies(phrase))     # {'what': 1, 'he': 1, 'had': 4, 'an': 1, 'affect': 1, 'on': 1, 'me': 1}
    it_is = 'it is what it is is it not'
    print(frequencies(it_is))      # {'it': 3, 'is': 3, 'what': 1, 'not': 1}

    unik_text = 'i denna text återkommer inget av orden mer än en gång'
    print(frequencies(unik_text))
    # {'i': 1, 'denna': 1, 'text': 1, 'återkommer': 1, 'inget': 1, 'av': 1, 'orden': 1, 'mer': 1, 'än': 1, 'en': 1, 'gång': 1}

    jag_drömde_text = 'i natt jag drömde något som jag aldrig drömt förut jag drömde det var fred på jord och alla krig var slut'
    print(frequencies(jag_drömde_text))
    # {'i': 1, 'natt': 1, 'jag': 3, 'drömde': 2, 'något': 1, 'som': 1, 'aldrig': 1, 'drömt': 1, 'förut': 1, 'det': 1, 'var': 2, 'fred': 1, 'på': 1, 'jord': 1, 'och': 1, 'alla': 1, 'krig': 1, 'slut': 1}
