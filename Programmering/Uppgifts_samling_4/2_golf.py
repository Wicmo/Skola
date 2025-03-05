# För ett hål på en golfbana är par det antal slag som en duktig spelare förväntas behöva.
# Följande termer används för att jämföra en spelares resultat i förhållande till par:
# albatross - tre slag under par
# eagle - två slag under par
# birdie - ett slag under par
# par - antalet slag är lika med par
# bogey - ett slag över par
# Komplettera följande funktion så att den för givet par och antal slag returnerar rätt term.
# Termen ges av en av strängarna "albatross", "eagle", "birdie", "par" eller "bogey".
# Programmet behöver inte hantera några andra kombinationer, eller felaktig input.
def golf_term(par, strokes):
    diff = par - strokes
    if diff == 3:
        return 'albatross'
    elif diff == 2:
        return 'eagle'
    elif diff == 1:
        return 'birdie'
    elif diff == 0:
        return 'par'
    elif diff == -1:
        return 'bogey'


if __name__ == '__main__':
    print(golf_term(4, 3))      # birdie
    print(golf_term(3, 3))      # par

    print(golf_term(2, 2))      # par
    print(golf_term(3, 3))      # par
    print(golf_term(4, 4))      # par
    print(golf_term(10, 10))    # par
    print(golf_term(154, 154))  # par

    print(golf_term(5, 2))      # albatross
    print(golf_term(6, 3))      # albatross
    print(golf_term(5, 3))      # eagle
    print(golf_term(6, 4))      # eagle
    print(golf_term(3, 2))      # birdie
    print(golf_term(5, 4))      # birdie

    print(golf_term(7, 4))      # albatross
    print(golf_term(4, 2))      # eagle
    print(golf_term(4, 3))      # birdie
    print(golf_term(5, 5))      # par
    print(golf_term(3, 4))      # bogey
    print(golf_term(2, 3))      # bogey
    print(golf_term(1, 2))      # bogey
