# En n x m-matris är en rektangulär matris med n rader och m kolumner.
# I Python kan en matris representeras av en nästlad lista, alltså en lista vars element är listor.
# Skriv en funktion som tar två positiva heltal n och m returnerar en matris av storleken n x m,
# representerad av en nästlad lista. Matrisens alla element ska vara lika med 0.
def zeroes(n, m):
    mat = []
    for i in range(n):
        mat.append([])
        for j in range(m):
            mat[i].append(0)
    return mat


if __name__ == '__main__':
    print(zeroes(3, 2))    # [[0, 0], [0, 0], [0, 0]]
    print(zeroes(2, 3))    # [[0, 0, 0], [0, 0, 0]]
    n, m = 5, 7
    matrix = zeroes(n, m)
    print(not any(any(matrix[i]) for i in range(n)))
