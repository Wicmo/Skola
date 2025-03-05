# En tabell kan representeras som en nästlad lista, alltså en lista vars element
# är listor. Varje rad i tabellen motsvaras av en lista i listan. Antag att vi
# vill kunna fylla i en given kolumn i en tabell med värden från en lista.

# values: 1 2 3
# column: 1
# table:
# 0 0 0 0        0 1 0 0
# 0 0 0 0   ->   0 2 0 0
# 0 0 0 0        0 3 0 0

# Skriv en funktion som tar en nästlad lista table, en lista values med värden
# samt ett kolumnnummer c som input och sätter kolumnens element lika med värdena
# i values. Funktionen ska alltså förändra tabellens innehåll men inte returnera
# något.

# Du kan förutsätta att alla rader i table har lika många element, att values
# har lika många element som antalet rader i table samt att c svarar mot en
# kolumn i tabellen.

def set_column(table, values, c):
    for r in range(len(table)):
        table[r][c] = values[r]


if __name__ == '__main__':
    mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    col = [4, 8, 3]
    set_column(mat, col, 1)
    print(mat)       # [[0, 4, 0], [0, 8, 0], [0, 3, 0]]

    mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    set_column(mat, [1, 2, 3], 1)
    print(mat)       # [[0, 1, 0, 0], [0, 2, 0, 0], [0, 3, 0, 0]]

    import random
    n, m = 4, 4
    chart = []
    for i in range(n):
        chart.append(random.sample(range(11, 100), m))
    print(chart)

    print(random.sample(range(1, 10), 3))
    print(random.sample(range(1, 10), 7))
