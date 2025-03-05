# En enhetsmatris är en kvadratisk nxn-matris som har ettor längs med huvuddiagonalen (från övre
# vänstra hörnet till nedre högra hörnet) och nollor överallt annars.
# I Python kan en matris representeras av en nästlad lista, alltså en lista vars element är listor.
# Skriv en funktion som tar ett positivt heltal n och returnerar en enhetsmatris av storleken n x n,
# representerad av en nästlad lista.
def enhetsmatris(n):
    mat = []
    for i in range(n):
        mat.append([])
        for j in range(n):
            if i == j:
                mat[i].append(1)
            else:
                mat[i].append(0)
    return mat


if __name__ == '__main__':
    print(enhetsmatris(3))    # [[1, 0, 0], [0, 1, 0], [0, 0, 1]]