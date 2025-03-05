# En tabell kan representeras som en nästlad lista, alltså en lista vars element
# är listor. Varje rad i tabellen motsvaras av en lista i listan. Antag att vi
# vill summera talen i en given kolumn i en tabell.
# Ex:
# column: 1
# table:  0 3 0 0
#         0 1 0 0
#         0 2 0 0
#           =
# result:   6
#
# Skriv en funktion som tar en nästlad lista table och ett kolumnnummer c som
# input och summerar den givna kolumnens element. Funktionen ska alltså
# returnera ett värde men inte ändra tabellens innehåll.
# Du kan anta att alla rader i table har lika många element och att c svarar
# mot en kolumn i table.

def sum_column(table, c):
    res = 0
    for r in range(len(table)):
        res += table[r][c]
    return res


if __name__ == '__main__':
    tabell1 = [[13, 7, 25, 83, 16], [8, 18, 47, 23, 3], [8, 0, 12, 28, 14]]
    print(sum_column(tabell1, 2))    # 84 (= 25 + 47 + 12)
    print(sum_column(tabell1, 4))    # 33 (= 16 +  3 + 14)
    tabell2 = [[5, 2, 8], [4, 4, 7], [2, 6, 1], [8, 6, 2]]
    print(sum_column(tabell2, 0))    # 19 (= 5 + 4 + 2 + 8)
    print(sum_column(tabell2, 1))    # 18 (= 2 + 4 + 6 + 6)

    t1 = [[36, 36, 36, 36], [6, 6, 6, 6], [54, 54, 54, 54], [46, 46, 46, 46], [80, 80, 80, 80]]
    t2 = [[58, 58, 58], [51, 51, 51], [46, 46, 46], [41, 41, 41], [42, 42, 42], [52, 52, 52]]
    t3 = [[1, 1, 1, 1], [17, 17, 17, 17], [16, 16, 16, 16], [0, 0, 0, 0]]
    t4 = [[42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]]
    print(sum_column(t1, 1))         # 222
    print(sum_column(t2, 2))         # 290
    print(sum_column(t3, 3))         # 34
    print(sum_column(t4, 7))         # 42

    t1 = [[84, 68, 22, 43], [25, 23, 75, 89], [65, 76, 70, 86], [42, 54, 44, 5], [16, 64, 43, 91]]
    t2 = [[42, 0, 17], [82, 14, 15], [89, 3, 8], [35, 63, 27], [14, 76, 74], [46, 18, 57]]
    t3 = [[78, 90, 41, 65, 68, 38], [36, 1, 16, 16, 25, 74], [84, 55, 35, 11, 11, 0]]
    t4 = [[0, 0, 2, 0, 2, 5], [3, 5, 5, 2, 3, 2], [4, 1, 2, 4, 4, 3]]
    print(sum_column(t1, 3))         # 314
    print(sum_column(t2, 0))         # 308
    print(sum_column(t3, 4))         # 104
    print(sum_column(t4, 5))         # 10